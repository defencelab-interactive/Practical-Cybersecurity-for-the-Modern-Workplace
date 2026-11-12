from playwright.sync_api import sync_playwright
B='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/'
FILES=['02a-verification-card','04b-turn-on-mfa','06b-link-inspector','07b-home-wifi','08b-lost-phone']
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in FILES:
        pg=b.new_page(viewport={'width':1600,'height':1000}); errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(B+f+'.html'); pg.wait_for_timeout(500)
        # compare right edges of block-level prose vs cards
        edges=pg.evaluate("""() => {
          const sels=['.lede','.tier-w','.sub','.stale','.acct','.dec','.managed','.step','.card','.note'];
          const out={};
          sels.forEach(s=>{const e=document.querySelector(s); if(e){const r=e.getBoundingClientRect();
            out[s]=Math.round(r.left)+'-'+Math.round(r.right);}});
          return out;}""")
        print(f'{f:24}', edges, 'errors:',errs or '')
        pg.close()
    # mobile sanity
    for f in FILES:
        pg=b.new_page(viewport={'width':390,'height':844})
        pg.goto(B+f+'.html'); pg.wait_for_timeout(400)
        print(f'{f:24} mobile h-scroll:', pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
        pg.close()
    b.close()
