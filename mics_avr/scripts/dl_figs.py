import json,os,sys,urllib.request,time
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__))))
from figsel import SEL
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG=os.path.join(BASE,'figures'); os.makedirs(FIG,exist_ok=True)
idx=json.load(open(os.path.join(BASE,'figs_index.json')))
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
ok=0
for fid,pmc,i,cap in SEL:
    a=idx.get(pmc)
    if not a or i>=len(a['figs']): print('MISS',fid,pmc,i); continue
    url=a['figs'][i]['img']; ext=os.path.splitext(url)[1] or '.jpg'
    fn=f"mics_{fid}_{pmc}{ext}"; p=os.path.join(FIG,fn)
    if os.path.exists(p) and os.path.getsize(p)>3000: ok+=1; continue
    try:
        r=urllib.request.Request(url,headers=UA)
        d=urllib.request.urlopen(r,timeout=90).read()
        open(p,'wb').write(d); ok+=1
        print(f"{fid:6s} {fn:34s} {len(d)//1024:5d} KB")
    except Exception as e: print('ERR',fid,pmc,e)
    time.sleep(0.4)
print('downloaded/present:',ok,'/',len(SEL))
