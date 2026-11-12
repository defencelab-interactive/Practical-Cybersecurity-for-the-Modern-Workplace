from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/13a-first-moves.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1100},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('situations:',pg.locator('.sit').count(),'| spine steps:',pg.locator('.sp-s').count())
    print('default panel:',pg.locator('.panel h2').inner_text())
    print('steps shown:',pg.locator('.st').count(),'| has "Not this":',pg.locator('.never-tag').count()==1)
    # cycle all five
    for i in range(5):
        pg.locator(f'[data-sit="{i}"]').click(); pg.wait_for_timeout(200)
        h=pg.locator('.panel h2').inner_text(); n=pg.locator('.st').count()
        on=pg.locator('.sit.on').count()
        print(f'  sit {i}: steps={n} selected={on} | {h[:52]}')
    # no storage, no print, no return-visit promise
    src=open('bytes/13a-first-moves.html',encoding='utf-8').read()
    print('storage used:', 'localStorage' in src or 'window.storage' in src)
    print('print button:', 'window.print' in src)
    print('promises remembering:', 'remember' in src.lower())
    print('escape artefacts in output:', '\\u' in pg.inner_text('body'))
    pg.screenshot(path='build/b13a-top.png')
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(500)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg2.locator('[data-sit="4"]').click(); pg2.wait_for_timeout(300)
    pg2.screenshot(path='build/b13a-mobile.png')
    b.close()
print('errors:',errs or 'none')
