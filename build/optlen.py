import re,io,glob,statistics
rows=[]
for f in sorted(glob.glob('courses/*.html')):
    s=io.open(f,encoding='utf-8').read()
    # each opts:[ ... ] block
    for m in re.finditer(r"q:'((?:[^'\\]|\\.)*)',\s*\n?\s*opts:\s*\[(.*?)\]\]", s, re.S):
        q=m.group(1); block=m.group(2)+']'
        opts=re.findall(r"\['((?:[^'\\]|\\.)*)',([01])\]", block)
        if len(opts)<2: continue
        def clean(t):
            t=re.sub(r'<[^>]+>','',t)
            t=t.replace('\\u2019',"'").replace('\\u201C','"').replace('\\u201D','"').replace('\\u2014','-')
            return t
        lens=[(len(clean(t)),int(c),clean(t)) for t,c in opts]
        right=[l for l,c,_ in lens if c==1]
        wrong=[l for l,c,_ in lens if c==0]
        if not right or not wrong: continue
        r=right[0]; mw=statistics.mean(wrong); mx=max(wrong)
        rows.append((f.split('/')[-1],q[:46],r,round(mw),mx,r-mx,lens))
longest=sum(1 for r in rows if r[5]>0)
print(f'{len(rows)} questions | correct answer is the LONGEST option in {longest} of them ({round(longest/len(rows)*100)}%)')
print(f'mean correct {round(statistics.mean(r[2] for r in rows))} chars vs mean wrong {round(statistics.mean(r[3] for r in rows))}\n')
for fn,q,r,mw,mx,d,lens in sorted(rows,key=lambda x:-x[5]):
    if d>3:
        print(f'{fn[:22]:24} +{d:3}  correct={r:3} longest-wrong={mx:3} | {q}')
        for l,c,t in lens: print(f'      {"RIGHT" if c else "     "} {l:3}  {t[:88]}')
