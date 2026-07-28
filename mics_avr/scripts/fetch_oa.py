import os, re, sys, tarfile, urllib.request, io
from concurrent.futures import ThreadPoolExecutor
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(BASE,'oa_pkg')
rows=[l.rstrip('\n').split('\t') for l in open(os.path.join(BASE,'oa_status.tsv'))]
jobs=[(r[0], r[3]) for r in rows if len(r)>3 and r[1]=='OA' and r[3].endswith('.tar.gz')]
def dl(j):
    pmc,url=j
    url=url.replace('ftp://ftp.ncbi.nlm.nih.gov/','https://ftp.ncbi.nlm.nih.gov/')
    d=os.path.join(OUT,pmc)
    if os.path.isdir(d) and os.listdir(d): return f"{pmc}\tcached"
    try:
        req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        data=urllib.request.urlopen(req,timeout=120).read()
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as tf:
            tf.extractall(OUT)
        # rename extracted dir to pmc id
        for n in os.listdir(OUT):
            p=os.path.join(OUT,n)
            if os.path.isdir(p) and n.startswith('PMC') and n==pmc: break
        return f"{pmc}\tok"
    except Exception as e:
        return f"{pmc}\tERR\t{e}"
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(dl,jobs): print(r)
