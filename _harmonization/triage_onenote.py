#!/usr/bin/env python3
"""Tag imported/legacy notes with a Triage property (Work / Personal / Mixed / Unclear / Stub / Duplicate).
Usage: python3 triage_onenote.py <vault> [--apply]. Adds two properties only; bodies untouched; nothing is moved."""
import os, re, sys, json, hashlib, collections, yaml
ROOTS = ["01-Personal/Daily Notes", "01-Personal/04-Archives", "01-Personal/CY23H2 BUJO", "01-Personal/Quick Notes", "02-Work/Quick Notes 2"]
WORK = r"STACK|EHS|SOSPES|OSHA|JSA|MOP|CAB|LOTO|SPCC|arc flash|data center|incident|audit|ACOM|COMs?|COTs?|contractor|toolbox talk|Thyssenkrupp|TK|CyrusOne|Cyrus One|safety|forklift|OneSource|SharePoint|permit|inspection|compliance|site visit|1 on 1|one on one|Asana|Power ?BI|corrective action|near miss|PPE|confined space|fall protection|hot work|DEQ|EPA|Tier II|generator|UPS"
PERS = r"Rhett|Kelsey|Mom|Dad|baseball|pitching|recipe|vacation|mortgage|townhouse|birthday|school|doctor|dentist|grocery|church|Christmas|dinner|workout|gym|movie|DMV|family|wife|haircut|Spring Break|Alamo Bowl|resume|salary|application|interview prep|genealogy|Nuckolls Family|Kongs|laptop|podcast|book"
SITE = r"(?:ATL|NAL|NVA|TOR|POR|DFW|CHI|SVY)\d{2}[A-Z]"
def main():
    vault = sys.argv[1]; apply = "--apply" in sys.argv; os.chdir(vault)
    P = "02-Work/06-Work Person/STACK People"
    people = [f[:-3] for f in os.listdir(P) if f.endswith(".md") and not f.endswith((" MOC.md", " Hub.md")) and f[:-3] != "David Nuckolls"]
    wre = re.compile(r"(?<!\w)(" + WORK + "|" + SITE + "|" + "|".join(map(re.escape, people)) + r")(?!\w)")
    pre = re.compile(r"(?<!\w)(" + PERS + r")(?!\w)", re.I)
    notes = []
    for root in ROOTS:
        for r, d, fs in os.walk(root):
            d.sort()
            for f in sorted(fs):
                if not f.endswith(".md"): continue
                p = os.path.join(r, f).replace(os.sep, "/"); raw = open(p, encoding="utf-8", newline="").read()
                t = raw.replace("\r\n", "\n"); m = re.match(r"---\n(.*?)\n---[ \t]*(\n|$)", t, re.S)
                fm, body = (m.group(1), t[m.end():]) if m else (None, t)
                if fm is not None:
                    try:
                        if not isinstance(yaml.safe_load(fm), dict): fm, body = None, t; bad = True
                        else: bad = False
                    except Exception: fm, body = None, t; bad = True
                else: bad = t.startswith("---\n")
                notes.append(dict(p=p, raw=raw, fm=fm, body=body, bad=bad, stem=f[:-3]))
    groups = collections.defaultdict(list)
    for n in notes:
        core = re.sub(r"\s+", " ", n["body"]).strip(); n["core"] = core
        if len(core) >= 60: groups[hashlib.md5(core.encode()).hexdigest()].append(n)
    for g in groups.values():
        if len(g) > 1:
            g.sort(key=lambda n: ("05-Archives" in n["p"], len(n["p"])))
            for n in g[1:]: n["dup"] = g[0]["p"]
    stats = collections.Counter(); byroot = collections.defaultdict(collections.Counter); changes = []
    for n in notes:
        text = n["stem"] + "\n" + n["body"]
        w = list(dict.fromkeys(wre.findall(text))); pz = list(dict.fromkeys(x.capitalize() for x in pre.findall(text)))
        wn, pn = len(wre.findall(text)), len(pre.findall(text))
        if n.get("dup"): tri = "Duplicate"
        elif len(n["core"]) < 60: tri = "Stub"
        elif wn >= 2 and pn >= 2: tri = "Mixed"
        elif wn >= 2: tri = "Work"
        elif pn >= 1: tri = "Personal"
        else: tri = "Unclear"
        root = next(r for r in ROOTS if n["p"].startswith(r)); stats[tri] += 1; byroot[root][tri] += 1
        if n["fm"] is not None and re.search(r"^Triage:", n["fm"], re.M): continue
        if n["bad"]: stats["(skipped: leading --- block)"] += 1; continue
        sig = "; ".join(x for x in ("work: " + ", ".join(w[:6]) if w else "", "personal: " + ", ".join(pz[:6]) if pz else "") if x)
        add = [f"Triage: {tri}"] + ([f"Triage Signals: {json.dumps(sig, ensure_ascii=False)}"] if sig else []) + ([f"Duplicate Of: {json.dumps('[[' + n['dup'][:-3] + ']]', ensure_ascii=False)}"] if n.get("dup") else [])
        fm = (n["fm"] + "\n" if n["fm"] else "") + "\n".join(add)
        assert isinstance(yaml.safe_load(fm), dict)
        out = "---\n" + fm + "\n---\n" + n["body"]
        if "\r\n" in n["raw"]: out = out.replace("\n", "\r\n")
        changes.append((n["p"], n["raw"], out))
    print(("APPLIED" if apply else "DRY RUN"), "| notes scanned:", len(notes), "| to tag:", len(changes)); print(dict(stats))
    for r in ROOTS: print(" ", r, dict(byroot[r]))
    if apply:
        bk = os.path.join("_harmonization", "backup-triage.json")
        old = json.load(open(bk, encoding="utf-8")) if os.path.exists(bk) else {}
        old.update({p: raw for p, raw, _ in changes if p not in old}); json.dump(old, open(bk, "w", encoding="utf-8"), ensure_ascii=False)
        for p, _, out in changes: open(p, "w", encoding="utf-8", newline="").write(out)
if __name__ == "__main__": main()
