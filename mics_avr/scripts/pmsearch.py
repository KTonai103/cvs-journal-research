import sys, json, urllib.parse, urllib.request, re, time
def get(url):
    req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace')
def search(db, term, retmax=40):
    u=f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&retmax={retmax}&term="+urllib.parse.quote(term)
    t=get(u); return re.findall(r'<Id>(\d+)</Id>', t), re.search(r'<Count>(\d+)</Count>',t).group(1)
def summ(db, ids):
    if not ids: return []
    u=f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db={db}&retmode=json&id="+",".join(ids)
    d=json.loads(get(u))['result']
    out=[]
    for i in d['uids']:
        r=d[i]
        out.append({'id':i,'title':r.get('title','').replace('\n',' '),
                    'journal':r.get('fulljournalname') or r.get('source',''),
                    'year':(r.get('pubdate') or '')[:4],
                    'doi':next((x['value'] for x in r.get('articleids',[]) if x['idtype']=='doi'),''),
                    'pmc':next((x['value'] for x in r.get('articleids',[]) if x['idtype'] in('pmc','pmcid')),'')})
    return out
if __name__=='__main__':
    db=sys.argv[1]; term=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 40
    ids,cnt=search(db,term,n)
    print(f"### {term}\n### count={cnt} shown={len(ids)}")
    for r in summ(db,ids):
        print(f"{r['id']} | {r['pmc']} | {r['year']} | {r['journal'][:38]} | {r['title'][:120]} | {r['doi']}")
