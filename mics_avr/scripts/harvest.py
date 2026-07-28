#!/usr/bin/env python3
"""Harvest figure images + captions from PMC article HTML (CC-licensed OA articles only)."""
import re, os, sys, json, urllib.request
from concurrent.futures import ThreadPoolExecutor
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG=os.path.join(BASE,'figures'); os.makedirs(FIG,exist_ok=True)
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
def get(u,b=False):
    r=urllib.request.Request(u,headers=UA)
    d=urllib.request.urlopen(r,timeout=90).read()
    return d if b else d.decode('utf-8','replace')
def strip(s):
    s=re.sub(r'<[^>]+>',' ',s); return re.sub(r'\s+',' ',s).strip()
def one(row):
    pmc,lic=row
    try: h=get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")
    except Exception as e: return pmc,{'error':str(e)}
    t=re.search(r'<title>(.*?)</title>',h,re.S)
    title=strip(t.group(1)).replace(' - PMC','') if t else ''
    cit=re.search(r'<meta name="citation_journal_title" content="([^"]*)"',h)
    yr=re.search(r'<meta name="citation_publication_date" content="([^"]*)"',h)
    doi=re.search(r'<meta name="citation_doi" content="([^"]*)"',h)
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
    return pmc,{'license':lic,'title':title,'journal':cit.group(1) if cit else '',
                'year':(yr.group(1) if yr else '')[:4],'doi':doi.group(1) if doi else '',
                'authors':au[:3],'nfigs':len(figs),'figs':figs}
rows=[l.rstrip('\n').split('\t') for l in open(os.path.join(BASE,'oa_list.tsv'))]
out={}
with ThreadPoolExecutor(6) as ex:
    for pmc,d in ex.map(one,rows):
        out[pmc]=d
        if 'error' in d: print(f"ERR {pmc} {d['error']}",file=sys.stderr); continue
        print(f"\n== {pmc} [{d['license']}] {d['year']} {d['journal'][:34]} | {d['title'][:90]}")
        for f in d['figs']:
            print(f"   {f['label'] or '-':10s} {f['caption'][:150]}")
json.dump(out,open(os.path.join(BASE,'figs_index.json'),'w'),ensure_ascii=False,indent=1)
