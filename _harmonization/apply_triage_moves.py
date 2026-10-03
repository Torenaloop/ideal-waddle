#!/usr/bin/env python3
"""Act on the Triage property. Usage: python3 apply_triage_moves.py <vault> [--apply]
Work (in 01-Personal) -> 02-Work/04 - Work Archives/Imported from Personal/<year>/
Personal (in 02-Work/Quick Notes 2) -> 01-Personal/Quick Notes/
Duplicate + Stub -> _to_delete/<original path>   (stubs holding an image/embed are left in place)
Mixed / Unclear are not touched. Every move is logged to moves.jsonl (old -> new) so it can be undone. Resumable."""
import os, re, sys, json, datetime
ROOTS = ["01-Personal/Daily Notes", "01-Personal/04-Archives", "01-Personal/CY23H2 BUJO", "01-Personal/Quick Notes", "02-Work/Quick Notes 2"]
def pdate(s):
    m = re.search(r'(?<!\d)(20\d\d)[-.](\d{1,2})[-.](\d{1,2})(?!\d)', s)
    if m: y, mo, d = m.groups()
    else:
        m = re.search(r'(?<!\d)(\d{1,2})[-.](\d{1,2})[-.](20\d\d|\d\d)(?!\d)', s)
        if not m: return None
        mo, d, y = m.groups(); y = y if len(y) == 4 else "20" + y
    try: return datetime.date(int(y), int(mo), int(d)).isoformat()
    except ValueError: return None
def main():
    vault = sys.argv[1]; apply = "--apply" in sys.argv; os.chdir(vault)
    log = os.path.join("_harmonization", "moves.jsonl")
    plan, kept, used = [], 0, set()
    def free(dest):
        base, ext = os.path.splitext(dest); i = 2; d = dest
        while os.path.exists(d) or d.lower() in used: d = f"{base} ({i}){ext}"; i += 1
        used.add(d.lower()); return d
    for root in ROOTS:
        for r, dirs, fs in os.walk(root):
            dirs.sort()
            for f in sorted(fs):
                if not f.endswith(".md"): continue
                p = os.path.join(r, f).replace(os.sep, "/")
                t = open(p, encoding="utf-8", errors="ignore").read().replace("\r\n", "\n")
                m = re.match(r"---\n(.*?)\n---[ \t]*(\n|$)", t, re.S)
                if not m: continue
                tm = re.search(r"^Triage: (\w+)", m.group(1), re.M)
                if not tm: continue
                tri, body = tm.group(1), t[m.end():]
                if tri == "Work" and root.startswith("01-Personal"):
                    d = pdate(f[:-3]) or next((pdate(x) for x in reversed(p.split("/")[:-1]) if not x.startswith("Week") and pdate(x)), None)
                    plan.append(("work", p, free(f"02-Work/04 - Work Archives/Imported from Personal/{d[:4] if d else 'Undated'}/{f}"), d))
                elif tri == "Personal" and root.startswith("02-Work"):
                    plan.append(("personal", p, free(f"01-Personal/Quick Notes/{f}"), None))
                elif tri in ("Duplicate", "Stub"):
                    if tri == "Stub" and re.search(r"!\[|\.(png|jpe?g|pdf|docx?|xlsx?|pptx?)\b", body, re.I): kept += 1; continue
                    dest = "_to_delete/" + p
                    if len(dest) > 200: dest = free("_to_delete/_long paths/" + f)
                    plan.append((tri.lower(), p, dest, None))
    c = {}
    for k, *_ in plan: c[k] = c.get(k, 0) + 1
    print(("APPLY" if apply else "DRY RUN"), c, "| stubs kept in place (hold an image or file):", kept)
    if not apply: return
    done = 0
    with open(log, "a", encoding="utf-8") as L:
        for kind, src, dest, d in plan:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if os.path.exists(dest): continue
            L.write(json.dumps({"kind": kind, "from": src, "to": dest}, ensure_ascii=False) + "\n"); L.flush()
            os.rename(src, dest); done += 1
            if kind == "work":
                raw = open(dest, encoding="utf-8", newline="").read(); nl = "\r\n" if "\r\n" in raw else "\n"
                add = [x for x in (None if re.search(r"^PARA:", raw, re.M) else "PARA: Archives",
                                   None if (not d or re.search(r"^Date:", raw, re.M)) else f"Date: {d}",
                                   None if (not pdate(os.path.basename(dest)[:-3]) or re.search(r"^type:", raw, re.M)) else "type: daily-note") if x]
                if add: open(dest, "w", encoding="utf-8", newline="").write(raw.replace("---" + nl, "---" + nl + nl.join(add) + nl, 1))
    print("moved this run:", done)
if __name__ == "__main__": main()
