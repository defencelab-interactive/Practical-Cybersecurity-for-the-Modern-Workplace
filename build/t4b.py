from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/04b-turn-on-mfa.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1000},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('accounts:',pg.locator('.acct').count(),'| tiers:',pg.locator('.tier').count())
    print('progress:',pg.inner_text('#pn'))
    print('real links:',pg.locator('a.acct-go').count(),'| search-only:',pg.locator('span.acct-go').count())
    hrefs=pg.evaluate("[...document.querySelectorAll('a.acct-go')].map(a=>a.href)")
    for h in hrefs: print('  ->',h)
    # tick a few
    pg.locator('[data-tick="google"]').click(); pg.wait_for_timeout(150)
    pg.locator('[data-tick="apple"]').click(); pg.wait_for_timeout(250)
    print('after 2 ticks:',pg.inner_text('#pn'),'| bar:',pg.evaluate("document.getElementById('pb').style.width"))
    # add own
    pg.fill('#ownin','Company VPN'); pg.locator('#ownadd').click(); pg.wait_for_timeout(300)
    print('after add:',pg.inner_text('#pn'),'| own rows:',pg.locator('#ownlist .acct').count())
    print('ticks survived re-render:',pg.locator('.acct.on').count())
    pg.locator('[data-rm]').first.click(); pg.wait_for_timeout(250)
    print('after remove:',pg.inner_text('#pn'),'| own rows:',pg.locator('#ownlist .acct').count())
    pg.screenshot(path='build/b4b-top.png',clip={'x':0,'y':0,'width':1100,'height':1000})
    pg.evaluate("document.querySelector('h2').scrollIntoView({block:'start'})"); pg.wait_for_timeout(300)
    pg.screenshot(path='build/b4b-dec.png')
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(600)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg2.screenshot(path='build/b4b-mobile.png')
    b.close()
print('errors:',errs or 'none')
