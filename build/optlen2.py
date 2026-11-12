from playwright.sync_api import sync_playwright
import glob,statistics,os
rows=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in sorted(glob.glob('courses/*.html')):
        pg=b.new_page()
        pg.goto('file://'+os.path.abspath(f)); pg.wait_for_timeout(400)
        pg.evaluate('document.querySelectorAll(".node").forEach(n=>n.classList.remove("locked"))')
        data=pg.evaluate("""() => {
          const out=[];
          document.querySelectorAll('.spot-opts').forEach(g=>{
            const opts=[...g.querySelectorAll('.spot-opt')].map(o=>({
              t:o.innerText.trim(), i:+o.dataset.j, n:+o.dataset.opt}));
            if(opts.length) out.push(opts);
          });
          return out;}""")
        # correctness from NODES
        correct=pg.evaluate("""() => {
          const m={};
          NODES.forEach((nd,i)=>{ const s=nd.spot;
            if(s&&s.opts) m[i]=s.opts.findIndex(o=>o[1]===1); });
          return m;}""")
        for grp in data:
            n=grp[0]['n']
            ci=correct.get(str(n), correct.get(n))
            if ci is None or ci<0: continue
            lens=[(len(o['t']),o['i']==ci,o['t']) for o in grp]
            r=[l for l,c,_ in lens if c]; w=[l for l,c,_ in lens if not c]
            if not r or not w: continue
            rows.append((os.path.basename(f),n,r[0],max(w),statistics.mean(w),lens))
        pg.close()
    b.close()
longest=sum(1 for r in rows if r[2]>r[3])
print(f'{len(rows)} questions | correct is the longest option in {longest} ({round(longest/len(rows)*100)}%)')
print(f'mean correct {round(statistics.mean(r[2] for r in rows))} vs mean wrong {round(statistics.mean(r[4] for r in rows))}\n')
for fn,n,r,mx,mw,lens in sorted(rows,key=lambda x:-(x[2]-x[3])):
    if r-mx>2:
        print(f'{fn[:22]:24} node {n}  +{r-mx}')
        for l,c,t in lens: print(f'      {"RIGHT" if c else "     "} {l:3}  {t}')
        print()
