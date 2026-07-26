import re,os,glob
src="pdf_text"; dst="pdf_text_clean"; os.makedirs(dst,exist_ok=True)
CUT=re.compile(r'^\s*(References|REFERENCES|Bibliography|Literatur)\s*:?\s*$',re.M)
tot_in=tot_out=0
for p in sorted(glob.glob(src+"/*.txt")):
    t=open(p,errors="ignore").read(); tot_in+=len(t)
    # 参照文献以降を落とす（末尾40%以降に出現する見出しのみ対象）
    ms=[m for m in CUT.finditer(t) if m.start()>len(t)*0.35]
    if ms: t=t[:ms[-1].start()]
    # 番号付き参照行の塊（"12. Author AB, ... 2019;..." 形式）を除去
    t=re.sub(r'\n\s*\d{1,3}\.\s+[A-Z][^\n]{40,}\d{4}[^\n]{0,80}\n','\n',t)
    # ダウンロード透かし・繰り返しフッタ
    t=re.sub(r'Downloaded from [^\n]*\n','',t)
    t=re.sub(r'https?://\S+\n','',t)
    t=re.sub(r'\n{3,}','\n\n',t)
    tot_out+=len(t)
    open(os.path.join(dst,os.path.basename(p)),"w").write(t)
print(f"{tot_in/1e6:.2f}MB -> {tot_out/1e6:.2f}MB")
