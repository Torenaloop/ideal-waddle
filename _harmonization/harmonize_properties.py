#!/usr/bin/env python3
"""Harmonize frontmatter property names/values in 02-Work (archives excluded).

Usage (run from anywhere):
  python3 harmonize_properties.py <vault>            # dry run, writes report only
  python3 harmonize_properties.py <vault> --apply    # apply + write backup manifest
  python3 harmonize_properties.py <vault> --restore <backup.json>

Idempotent: a second --apply changes nothing. Only frontmatter is touched, plus
property names inside ```dataview blocks. Convention: Title Case property names,
except the reserved lowercase keys in KEEP.
"""
import os, re, sys, json, datetime, collections

SCOPE = "02-Work"
SKIP_DIRS = ("04 - Work Archives", "Quick Notes 2", "03 - Work Resources")
KEEP = {"type", "tags", "aliases", "cssclasses", "created", "updated", "title",
        "source", "author", "description", "published"}
RENAME = {
    "status": "Status", "priority": "Priority", "para": "PARA",
    "Due-Date": "Due Date", "due_date": "Due Date",
    "Start-Date": "Start Date", "start_date": "Start Date",
    "start": "Start Date", "due": "Due Date",
    "date": "Date", "meeting_date": "Date",
    "participants": "People", "Participants": "People", "Attendees": "People",
    "Work Person": "People", "person": "People", "people": "People",
    "meeting_type": "Meeting Type",
    "site": "Site", "site_code": "Site",
    "email": "Email", "Person's email": "Email", "Person's title": "Job Title",
    "Person's company": "Company", "manager": "Manager",
    "sender": "Sender", "From": "Sender", "from": "Sender",
    "sender_email": "Sender Email",
    "recipient": "Recipient", "To": "Recipient", "to": "Recipient",
    "subject": "Subject", "action_items": "Action Items",
    "project": "Project", "projects": "Project",
    "dependencies": "Dependencies", "stakeholders": "Stakeholders",
    "parent_goal": "Parent Goal", "child_goal": "Child Goal",
    "Related-To": "Related", "Related to": "Related",
    "Type": "Category", "ehs_support": "EHS Support",
}
VALUES = {
    "Status": {"in-progress": "In Progress", "in progress": "In Progress",
               "complete": "Complete", "completed": "Complete", "done 🙌": "Complete",
               "not-started": "Not Started", "not started": "Not Started",
               "active": "Active", "unprocessed": "Unprocessed",
               "cancelled": "Cancelled", "future": "Future", "published": "Published"},
    "Priority": {"critical": "Critical", "high": "High", "medium": "Medium", "low": "Low"},
    "PARA": {"project": "Projects", "projects": "Projects", "area": "Areas",
             "areas": "Areas", "resource": "Resources", "resources": "Resources",
             "archive": "Archives", "archives": "Archives"},
}
SITE_FOLDERS = {"ATL01A": "ATL01A", "NAL01A": "NAL01A", "NVA01A": "NVA01A",
                "NVA02D-E": "NVA02D-E", "NVA05A": "NVA05A", "NVA05D": "NVA05D",
                "NVA06A-B": "NVA06A", "TOR01A": "TOR01A"}
SITE_PATHS = {"ATL01A": "ATL01A", "NAL01A": "NAL01A", "NVA01A": "NVA01A", "NVA02D-E": "NVA02D-E",
              "NVA05A": "NVA05A", "NVA05D": "NVA05D", "NVA06A": "NVA06A-B", "TOR01A": "TOR01A"}
def site_link(c):
    """Full-path link: Notion/ holds same-named site notes, so bare [[CODE]] is ambiguous."""
    return f'"[[02-Work/02 - Work Areas/{SITE_PATHS[c]}/{c}|{c}]]"' if c in SITE_PATHS else f'"[[{c}]]"'
SITE_RE = re.compile(r"^[A-Z]{3}\d{2}[A-Z](-[A-Z])?$")
KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9 _'\-\.]{0,39}):(\s.*|)$")
EMPTY = {"", '""', "''", "[]", "null", "~"}


def title_case(k):
    if k in KEEP or k in RENAME.values(): return k
    if re.fullmatch(r"[a-z0-9]+(_[a-z0-9]+)*", k):
        return " ".join(w.capitalize() for w in k.split("_"))
    return k

def split_note(text):
    m = re.match(r"---\n(.*?)\n---[ \t]*(\n|$)", text, re.S)
    if not m: return None, text
    return m.group(1), text[m.end():]

def parse(fm):
    """-> list of [key|None, [lines]] preserving raw text."""
    out = []
    for line in fm.split("\n"):
        km = KEY_RE.match(line)
        if km: out.append([km.group(1), [line]])
        elif out and (line.startswith((" ", "\t", "-")) or line.strip() == ""):
            out[-1][1].append(line)
        else: out.append([None, [line]])
    return out

def inline(e): return e[1][0].split(":", 1)[1].strip()
def is_empty(e): return inline(e) in EMPTY and not any(l.strip() for l in e[1][1:])
def unq(v): return v.strip().strip('"').strip("'").strip()
def set_inline(e, v): e[1][0] = f"{e[0]}: {v}"
def get(entries, k): return next((e for e in entries if e[0] == k), None)

def ensure(entries, k, v, log, top=False):
    e = get(entries, k)
    if e is None:
        entries.insert(0, [k, [f"{k}: {v}"]]) if top else entries.append([k, [f"{k}: {v}"]])
        log.append(f"add {k}: {v}")
    elif is_empty(e):
        e[1] = [f"{k}: {v}"]; log.append(f"fill {k}: {v}")

def file_date(name):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", name)
    if m: return "-".join(m.groups())
    m = re.search(r"(?<!\d)(\d{1,2})-(\d{1,2})-(\d{4})(?!\d)", name)
    if m:
        mo, d, y = m.groups()
        if 1 <= int(mo) <= 12 and 1 <= int(d) <= 31: return f"{y}-{int(mo):02d}-{int(d):02d}"
    return None

def process(rel, text, people):
    log, conflicts = [], []
    fm, body = split_note(text)
    entries = parse(fm) if fm is not None else []
    parts = rel.split("/")
    stem = parts[-1][:-3]
    top = parts[1] if len(parts) > 2 else ""

    # 1. renames / merges
    for e in list(entries):
        k = e[0]
        if k is None: continue
        new = RENAME.get(k) or title_case(k)
        if new == k: continue
        tgt = get(entries, new)
        if tgt is None:
            e[0] = new; e[1][0] = new + ":" + e[1][0].split(":", 1)[1]
            log.append(f"rename {k} -> {new}")
        elif is_empty(e) or (inline(e) == inline(tgt) and e[1][1:] == tgt[1][1:]):
            entries.remove(e); log.append(f"drop duplicate {k} (kept {new})")
        elif is_empty(tgt):
            i = entries.index(tgt); entries.remove(e)
            e[0] = new; e[1][0] = new + ":" + e[1][0].split(":", 1)[1]
            entries[i] = e; log.append(f"merge {k} -> {new}")
        else:
            conflicts.append(f"{k} vs {new}: both have values; left as-is")

    # 2. value normalisation
    for k, table in VALUES.items():
        e = get(entries, k)
        if e and len(e[1]) == 1:
            v = unq(inline(e))
            if v.lower() in table and table[v.lower()] != inline(e):
                set_inline(e, table[v.lower()]); log.append(f"{k}: {v} -> {table[v.lower()]}")
    e = get(entries, "Site")
    if e and len(e[1]) == 1 and SITE_RE.match(unq(inline(e))):
        v = unq(inline(e)); set_inline(e, site_link(v)); log.append(f"Site: {v} -> [[{v}]]")
    e = get(entries, "People")
    if e and len(e[1]) == 1:
        v = unq(inline(e))
        if v and "[[" not in v and v not in EMPTY:
            names = [n.strip() for n in v.split(",") if n.strip()]
            if any(n in people for n in names):
                e[1] = ["People:"] + [f'  - "[[{n}]]"' if n in people else f"  - {n}" for n in names]
                log.append("People: names -> list with links")

    # 3. derived properties
    typ = get(entries, "type")
    has_type = typ is not None and not is_empty(typ)
    def set_type(v):
        if not has_type: ensure(entries, "type", v, log, top=True)
    cat = get(entries, "Category")
    catv = unq(inline(cat)) if cat else ""
    in_1on1 = any("1 on 1" in p for p in parts[:-1])

    if top == "06-Work Person" and len(parts) > 3 and parts[2] == "STACK People":
        set_type("person")
    elif top == "06-Work Person" and get(entries, "Sender"):
        set_type("email")
    elif top == "05 - Work Meetings":
        if "MOC" in stem and not file_date(stem): set_type("moc")
        else:
            set_type("meeting")
            d = file_date(stem)
            if d: ensure(entries, "Date", d, log)
            if in_1on1: ensure(entries, "Meeting Type", "1-on-1", log)
            who = [p for p in people if p in stem]
            if in_1on1 and len(who) == 1: ensure(entries, "People", f'"[[{who[0]}]]"', log)
    elif top == "02 - Work Areas" and len(parts) > 3:
        site = SITE_FOLDERS.get(parts[2])
        if site:
            ensure(entries, "Site", site_link(site), log)
            ensure(entries, "PARA", "Areas", log)
            d = file_date(stem)
            if stem in (parts[2], site) or stem.endswith("_Site_Hub"): set_type("hub")
            elif stem.endswith("MOC"): set_type("moc")
            elif in_1on1 and d:
                set_type("meeting"); ensure(entries, "Date", d, log)
                ensure(entries, "Meeting Type", "1-on-1", log)
                who = [p for p in people if any(p in x for x in parts[3:-1])]
                if len(who) == 1: ensure(entries, "People", f'"[[{who[0]}]]"', log)
            else: set_type("site-note")
    elif top == "07 - Work Tasks":
        if "MOC" in stem: set_type("moc")
        elif get(entries, "Due Date"): set_type("task")
    elif top == "01 - Work Projects" and fm is not None:
        para = get(entries, "PARA")
        if get(entries, "Sender"): set_type("email")
        elif get(entries, "Goal Number") or "Goal" in catv: set_type("goal")
        elif "Hub" in catv: set_type("hub")
        elif para and unq(inline(para)) == "Projects" and get(entries, "Status"): set_type("project")

    # 4. dataview blocks: keep queries pointing at renamed properties
    def fix_dv(m):
        b = m.group(0)
        b2 = re.sub(r"\bType\b(?=\s*(=|,|\n))", "Category", b)
        b2 = re.sub(r"\bParticipants\b", "People", b2)
        if b2 != b: log.append("dataview query updated")
        return b2
    body2 = re.sub(r"```dataview\n.*?```", fix_dv, body, flags=re.S)

    if not log: return text, log, conflicts
    new_fm = "\n".join(l for e in entries for l in e[1])
    return f"---\n{new_fm}\n---\n{body2}", log, conflicts

def main():
    vault = sys.argv[1]; apply = "--apply" in sys.argv
    here = os.path.dirname(os.path.abspath(__file__))
    if "--restore" in sys.argv:
        bk = json.load(open(sys.argv[sys.argv.index("--restore") + 1], encoding="utf-8"))
        for rel, txt in bk.items(): open(os.path.join(vault, rel), "w", encoding="utf-8", newline="").write(txt)
        print(f"restored {len(bk)} files"); return
    pdir = os.path.join(vault, SCOPE, "06-Work Person", "STACK People")
    people = sorted((f[:-3] for f in os.listdir(pdir) if f.endswith(".md")), key=len, reverse=True)
    backup, report, stats, nconf = {}, [], collections.Counter(), 0
    for r, dirs, files in os.walk(os.path.join(vault, SCOPE)):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for f in sorted(files):
            if not f.endswith(".md"): continue
            p = os.path.join(r, f); rel = os.path.relpath(p, vault).replace(os.sep, "/")
            text = open(p, encoding="utf-8", newline="").read()
            crlf = "\r\n" in text
            if crlf:
                if text.count("\r\n") != text.count("\n"): report.append(f"SKIP (mixed line endings) {rel}"); continue
                text = text.replace("\r\n", "\n")
            new, log, conf = process(rel, text, people)
            if crlf: text, new = text.replace("\n", "\r\n"), new.replace("\n", "\r\n")
            for c in conf: report.append(f"CONFLICT {rel}: {c}"); nconf += 1
            if new == text: continue
            backup[rel] = text
            for l in log: stats[re.sub(r":.*", "", l) if l.startswith(("add", "fill")) else l.split(":")[0] if l[0].isupper() else l] += 1
            report.append(f"{rel}\n    " + "\n    ".join(log))
            if apply: open(p, "w", encoding="utf-8", newline="").write(new)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    mode = "APPLIED" if apply else "DRY RUN"
    head = [f"# Property harmonization report ({mode}, {ts})", "",
            f"Files changed: {len(backup)}   Conflicts left for review: {nconf}", "", "## Change counts"]
    head += [f"- {k}: {v}" for k, v in stats.most_common()] + ["", "## Per file", ""]
    open(os.path.join(here, f"report-{'applied' if apply else 'dryrun'}-{ts}.md"), "w", encoding="utf-8").write("\n".join(head + report))
    if apply and backup:
        json.dump(backup, open(os.path.join(here, f"backup-{ts}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    flagged = [x for x in report if x.startswith(("CONFLICT", "SKIP"))]
    print("\n".join(head[:-2])); print(f"flagged: {len(flagged)}"); print("\n".join(flagged[:25]))

if __name__ == "__main__": main()
