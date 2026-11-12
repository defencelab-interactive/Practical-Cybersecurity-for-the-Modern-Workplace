from playwright.sync_api import sync_playwright
import re
def w(t): return len(re.findall(r"[A-Za-z0-9$']+", t))
B=[('published','courses/03-physical-security.html'),
   ('tight','courses/03-physical-security-tight.html'),
   ('light','courses/03-physical-security-light.html'),
   ('min','build/03-min.html')]
root='/home/claude/practical-cybersecurity-for-the-modern-workplace/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    print(f'{"build":10} {"nodes":>5} {"stops":>6} {"base":>6} {"deep":>5} {"min@200wpm":>11} {"screens":>8}')
    for name,path in B:
        src=open(root+path,encoding='utf-8').read()
        a=src.index('const NODES='); z=src.index('\n];\n',a); n=src[a:z]
        tot=0
        for k in ['body','fb','note','why','how','itnote']:
            tot+=sum(w(m) for m in re.findall(k+r":'((?:[^'\\]|\\.)*)'",n))
        tot+=sum(w(m) for m in re.findall(r"steps:\[([^\]]*)\]",n))
        deep=sum(w(x) for x in re.findall(r"more:\{t:'(?:(?:[^'\\]|\\.)*)',\s*\n?\s*body:'((?:[^'\\]|\\.)*)'",n))
        base=tot-deep
        pg.goto('file://'+root+path); pg.wait_for_timeout(600)
        pg.evaluate('document.querySelectorAll(".node").forEach(n=>{n.classList.remove("locked");n.classList.add("seen")})')
        pg.evaluate('document.querySelectorAll(".spot-trigger").forEach(t=>t.click())')
        pg.evaluate('const e=document.querySelector(".endcard"); if(e)e.classList.remove("locked")')
        pg.wait_for_timeout(700)
        m=pg.evaluate('''()=>{const s=document.querySelector('.scroll');
          return {h:s.scrollHeight,vh:s.clientHeight,
            nodes:document.querySelectorAll('.node').length,
            stops:document.querySelectorAll('.spot-trigger,.checklist,.aud-bar,.flags-spot').length};}''')
        print(f'{name:10} {m["nodes"]:5} {m["stops"]:6} {base:6} {deep:5} {base/200:11.1f} {m["h"]/m["vh"]:8.1f}')
    b.close()
