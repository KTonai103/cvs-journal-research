import re,os,json,time,urllib.request,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE,'scripts')); from figsel import SEL
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
idx=json.load(open(os.path.join(BASE,'figs_index.json')))
pmcs=sorted({s[1] for s in SEL})
out={}
for p in pmcs:
    for a in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/",headers=UA),timeout=90).read().decode('utf-8','replace')
            if 'reCAPTCHA' in h[:4000]: raise RuntimeError('captcha')
            break
        except Exception as e:
            h=None; time.sleep(5)
    if not h: print('ERR',p); continue
    labs=[]
    for m in re.finditer(r'<figure\b(.*?)</figure>',h,re.S):
        b=m.group(1)
        if not re.search(r'src="https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^"]+?\.(?:jpg|jpeg|png|gif)"',b): continue
        lm=re.search(r'<(?:h[2-6]|span|strong|b)[^>]*>\s*((?:Fig(?:ure)?|Table|FIGURE)\.?\s*\d+[A-Za-z]?)[\.: ]',b)
        if not lm: lm=re.search(r'>\s*((?:Fig(?:ure)?|FIGURE)\.?\s*\d+)[\.: ]',b)
        labs.append(lm.group(1).strip() if lm else '')
    out[p]=labs
    print(p,labs)
    time.sleep(1.0)
json.dump(out,open(os.path.join(BASE,'fignums.json'),'w'))
