#!/usr/bin/env python3
"""Harvest figure metadata from PMC article HTML with retry; merge into figs_index.json."""
import re, os, sys, json, time, random, urllib.request
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'}
IDX=os.path.join(BASE,'figs_index.json')
out=json.load(open(IDX)) if os.path.exists(IDX) else {}
def get(u):
    r=urllib.request.Request(u,headers=UA)
    return urllib.request.urlopen(r,timeout=90).read().decode('utf-8','replace')
def strip(s):
    s=re.sub(r'<[^>]+>',' ',s); return re.sub(r'\s+',' ',s).strip()
rows=[l.rstrip('\n').split('\t') for l in open(os.path.join(BASE,'oa_all.tsv'))]
todo=[(p,l) for p,l in rows if p not in out or out[p].get('nfigs',0)==0 or 'reCAPTCHA' in out[p].get('title','')]
print(f"todo={len(todo)}",file=sys.stderr)
for pmc,lic in todo:
    for attempt in range(3):
        try:
            h=get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")
            if 'reCAPTCHA' in h[:4000]: raise RuntimeError('captcha')
            break
        except Exception as e:
            if attempt==2: print(f"ERR {pmc} {e}",file=sys.stderr); h=None
            else: time.sleep(4+random.random()*4)
    if not h: continue
    t=re.search(r'<meta name="citation_title" content="([^"]*)"',h) or re.search(r'<title>(.*?)</title>',h,re.S)
    title=strip(t.group(1)).replace(' - PMC','')
    j=re.search(r'<meta name="citation_journal_title" content="([^"]*)"',h)
    y=re.search(r'<meta name="citation_publication_date" content="([^"]*)"',h)
    d=re.search(r'<meta name="citation_doi" content="([^"]*)"',h)
    au=re.findall(r'<meta name="citation_author" content="([^"]*)"',h)
    figs=[]
    for m in re.finditer(r'<figure\b.*?</figure>',h,re.S):
        b=m.group(0)
        imgs=re.findall(r'src="(https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^"]+?\.(?:jpg|jpeg|png|gif))"',b)
        if not imgs: continue
        cap=re.search(r'<figcaption.*?>(.*?)</figcaption>',b,re.S)
        cap=strip(cap.group(1)) if cap else ''
        lbl=re.search(r'\b((?:Fig(?:ure)?|Table)\.?\s*\d+)',cap)
        figs.append({'label':lbl.group(1) if lbl else '','caption':cap[:900],'img':imgs[0]})
    out[pmc]={'license':lic,'title':title,'journal':j.group(1) if j else '','year':(y.group(1) if y else '')[:4],
              'doi':d.group(1) if d else '','authors':au[:3],'nfigs':len(figs),'figs':figs}
    print(f"\n== {pmc} [{lic}] {out[pmc]['year']} {out[pmc]['journal'][:32]} | {title[:88]}")
    for f in figs: print(f"   {f['label'] or '-':9s} {f['caption'][:150]}")
    time.sleep(1.2)
json.dump(out,open(IDX,'w'),ensure_ascii=False,indent=1)
print(f"\nTOTAL articles={len(out)}",file=sys.stderr)
