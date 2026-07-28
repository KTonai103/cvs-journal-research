import sys, re, urllib.request
from concurrent.futures import ThreadPoolExecutor
def get(u):
    r=urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"})
    return urllib.request.urlopen(r,timeout=45).read().decode('utf-8','replace')
def chk(pmc):
    try:
        x=get(f"https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmc}")
    except Exception as e:
        return f"{pmc}\tERR\t{e}"
    if '<error' in x:
        c=re.search(r'code="([^"]+)"',x)
        return f"{pmc}\tNO-OA\t{c.group(1) if c else '?'}\t-\t-"
    lic=re.search(r'license="([^"]*)"',x); tgz=re.search(r'href="([^"]*\.tar\.gz)"',x)
    pdf=re.search(r'format="pdf"\s+href="([^"]+)"',x)
    return f"{pmc}\tOA\t{lic.group(1) if lic else '?'}\t{tgz.group(1) if tgz else '-'}\t{pdf.group(1) if pdf else '-'}"
ids=[l.split()[0] for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(chk, ids): print(r)
