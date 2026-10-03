#!/usr/bin/env python3
"""Give 02-Work/04 - Work Archives the same properties as the rest of 02-Work.
Usage: python3 harmonize_archives.py <vault> [--apply]
Adds frontmatter only (type, Date, PARA, People, Site); note bodies are untouched. Idempotent."""
import os, re, sys, json, datetime, collections, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("h", os.path.join(here, "harmonize_properties.py"))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
A = "02-Work/04 - Work Archives"

def parse_date(s):
    m = re.search(r'(?<!\d)(20\d\d)[-.](\d{1,2})[-.](\d{1,2})(?!\d)', s)
    if m: y, mo, d = m.groups()
    else:
        m = re.search(r'(?<!\d)(\d{1,2})[-.](\d{1,2})[-.](20\d\d|\d\d)(?!\d)', s)
        if not m: return None
        mo, d, y = m.groups(); y = y if len(y) == 4 else "20" + y
    try: return datetime.date(int(y), int(mo), int(d)).isoformat()
    except ValueError: return None

def classify(parts, stem):
    top = parts[0] if parts else ""
    if re.match(r'\W*Week\b', stem) or stem in ("Table of Contents",) or re.fullmatch(r'(20\d\d|[A-Z][a-z]+ 20\d\d)', stem): return "moc"
    if "MOC" in stem: return "moc"
    if "Daily Meetings" in top: return "meeting"
    if "Daily Notes" in top or top.startswith("Week of"): return "daily-note"
    return None

def main():
    vault = sys.argv[1]; apply = "--apply" in sys.argv
    pdir = os.path.join(vault, "02-Work/06-Work Person/STACK People")
    people = [f[:-3] for f in os.listdir(pdir) if f.endswith(".md") and not f.endswith((" MOC.md", " Hub.md"))]
    pre = re.compile(r'(?<![\w\[])(' + "|".join(re.escape(p) for p in sorted(people, key=len, reverse=True)) + r')(?!\w)')
    site_re = re.compile(r'\b(' + "|".join(re.escape(s) for s in h.SITE_PATHS) + r')\b')
    backup, stats, rows = {}, collections.Counter(), []
    for r, dirs, files in os.walk(os.path.join(vault, A)):
        dirs.sort()
        for f in sorted(files):
            if not f.endswith(".md"): continue
            p = os.path.join(r, f); rel = os.path.relpath(p, vault).replace(os.sep, "/")
            raw = open(p, encoding="utf-8", newline="").read()
            crlf = "\r\n" in raw
            if crlf and raw.count("\r\n") != raw.count("\n"): stats["skipped mixed EOL"] += 1; continue
            t = raw.replace("\r\n", "\n")
            new, log, _ = h.process(rel, t, people)          # key renames / value normalisation
            fm, body = h.split_note(new)
            E = h.parse(fm) if fm is not None else []
            parts = rel[len(A) + 1:].split("/")[:-1]; stem = f[:-3]
            typ = classify(parts, stem)
            if typ and not h.get(E, "type"): h.ensure(E, "type", typ, log, top=True)
            d = parse_date(stem) or next((parse_date(x) for x in reversed(parts) if not re.match(r'\W*Week', x) and parse_date(x)), None)
            if d and typ != "moc": h.ensure(E, "Date", d, log)
            h.ensure(E, "PARA", "Archives", log)
            if typ == "meeting":
                names = list(dict.fromkeys(pre.findall(stem + "\n" + body)))[:12]
                if names and not h.get(E, "People"):
                    E.append(["People", ["People:"] + [f'  - "[[{n}]]"' for n in names]]); log.append("add People")
            if typ in ("meeting", "daily-note") and not h.get(E, "Site"):
                sites = set(site_re.findall(stem + "\n" + body))
                if len(sites) == 1: h.ensure(E, "Site", h.site_link(sites.pop()), log)
            if not log: continue
            fm_new = "\n".join(l for e in E for l in e[1])
            try:
                import yaml
                if not isinstance(yaml.safe_load(fm_new), dict): raise ValueError
            except Exception:
                stats["skipped (leading --- block is not valid properties)"] += 1; continue
            out = "---\n" + fm_new + "\n---\n" + body
            if crlf: out = out.replace("\n", "\r\n")
            if out == raw: continue
            backup[rel] = raw
            for l in log: stats[re.sub(r":.*", "", l)] += 1
            if apply: open(p, "w", encoding="utf-8", newline="").write(out)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    if apply and backup: json.dump(backup, open(os.path.join(here, f"backup-archives-{ts}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(("APPLIED" if apply else "DRY RUN"), "files changed:", len(backup))
    for k, v in stats.most_common(): print(f"  {k}: {v}")

if __name__ == "__main__": main()
