import json,sys,re,os
recs=json.load(open(os.path.join(os.path.dirname(os.path.abspath("q.py")),"corpus/records.json")))
pat=re.compile(sys.argv[1],re.I)
field=sys.argv[2] if len(sys.argv)>2 else "title"
out=[r for r in recs.values() if pat.search(r.get(field,"") if isinstance(r.get(field),str) else " ".join(r.get(field,[])))]
out.sort(key=lambda r:-int(r["year"] or 0))
for r in out:
    print(f"PMID {r['pmid']} | {r['year']} | {r['journal']} | {r['lastauthor']}\n    {r['title']}")
print(f"\n-- {len(out)} hits --")
