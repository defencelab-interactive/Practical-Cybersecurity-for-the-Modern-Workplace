from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/09a-what-your-profile-gives-away.html'
ANS=['keep','keep','trim','cut','cut','trim','cut','trim']
CYC=['keep','trim','cut']
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1200},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('elements:',pg.locator('[data-el]').count(),'| go disabled:',pg.locator('#go').is_disabled(),'| hint:',pg.inner_text('#bn'))
    print('results hidden at rest:',not pg.locator('#res').is_visible())
    # cycle one element through all states and back
    el=pg.locator('[data-el="0"]')
    for exp in CYC:
        el.click(); pg.wait_for_timeout(110)
        print(f'  cycle -> {exp}:', el.get_attribute('class').find('set-'+exp)>0)
    el.click(); pg.wait_for_timeout(110)
    print('  fourth click clears:', 'set-' not in el.get_attribute('class'))
    print('  hint after clearing:',pg.inner_text('#bn'))
    # sort all correctly
    for i,a in enumerate(ANS):
        for _ in range(CYC.index(a)+1):
            pg.locator(f'[data-el="{i}"]').click(); pg.wait_for_timeout(45)
    pg.wait_for_timeout(250)
    print('all sorted, go enabled:',not pg.locator('#go').is_disabled(),'| hint:',repr(pg.inner_text('#bn')))
    pg.screenshot(path='build/b9a-sorted.png')
    pg.locator('#go').click(); pg.wait_for_timeout(500)
    print('results shown:',pg.locator('#res').is_visible(),'| rows:',pg.locator('.r').count())
    print('verdict:',pg.inner_text('#fin h3'))
    print('mismatch labels shown:',pg.locator('.r-you').count(),'(expect 0 when all correct)')
    print('locked after reveal:',pg.locator('[data-el="0"]').get_attribute('class'))
    src=open('bytes/09a-what-your-profile-gives-away.html',encoding='utf-8').read()
    print('storage:', 'localStorage' in src, '| print:', 'window.print' in src, '| settings paths:', 'Settings →' in src)
    print('escape artefacts:', '\\u' in pg.inner_text('body'))
    pg.screenshot(path='build/b9a-result.png')
    # wrong path
    pg2=b.new_page(viewport={'width':1100,'height':900})
    pg2.goto(P); pg2.wait_for_timeout(400)
    for i in range(8):
        pg2.locator(f'[data-el="{i}"]').click(); pg2.wait_for_timeout(45)   # all -> keep
    pg2.locator('#go').click(); pg2.wait_for_timeout(400)
    print('all-keep verdict:',pg2.inner_text('#fin h3'),'| mismatches:',pg2.locator('.r-you').count())
    pg3=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg3.goto(P); pg3.wait_for_timeout(400)
    print('mobile h-scroll:',pg3.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg3.locator('[data-el="3"]').click(); pg3.wait_for_timeout(200)
    pg3.screenshot(path='build/b9a-mobile.png')
    b.close()
print('errors:',errs or 'none')
