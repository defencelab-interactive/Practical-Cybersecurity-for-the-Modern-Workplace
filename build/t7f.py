from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/07f-cafe-train-airport.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1150},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('options:',pg.locator('.p').count(),'| go disabled:',pg.locator('#go').is_disabled(),'| hint:',pg.inner_text('#bn'))
    print('ranking hidden at rest:',not pg.locator('#rank').is_visible())
    # pick the two common-wrong ones (wifi + usb) to exercise the 0-hit path
    pg.locator('[data-p="0"]').click(); pg.wait_for_timeout(120)
    print('after 1 pick:',pg.inner_text('#bn'),'| go disabled:',pg.locator('#go').is_disabled())
    pg.locator('[data-p="4"]').click(); pg.wait_for_timeout(150)
    print('after 2 picks, go enabled:',not pg.locator('#go').is_disabled())
    # third pick must be refused
    pg.locator('[data-p="2"]').click(); pg.wait_for_timeout(150)
    print('third pick refused:',pg.locator('.p.on').count()==2)
    # deselect and reselect
    pg.locator('[data-p="0"]').click(); pg.wait_for_timeout(120)
    print('deselect works:',pg.locator('.p.on').count()==1)
    pg.locator('[data-p="0"]').click(); pg.wait_for_timeout(150)
    pg.locator('#go').click(); pg.wait_for_timeout(500)
    print('ranking shown:',pg.locator('#rank').is_visible(),'| rows:',pg.locator('.r').count())
    print('order:',[r.inner_text() for r in pg.locator('.r-n').all()])
    print('yours tagged:',pg.locator('.r.yours').count())
    print('verdict:',pg.inner_text('#verdict h3')[:70])
    print('locked after reveal:',pg.locator('#picks').get_attribute('class'))
    src=open('bytes/07f-cafe-train-airport.html',encoding='utf-8').read()
    print('storage:', 'localStorage' in src, '| print:', 'window.print' in src)
    print('escape artefacts:', '\\u' in pg.inner_text('body'))
    pg.screenshot(path='build/b7f.png')
    # 2-hit path on a fresh load
    pg2=b.new_page(viewport={'width':1100,'height':900})
    pg2.goto(P); pg2.wait_for_timeout(400)
    pg2.locator('[data-p="1"]').click(); pg2.locator('[data-p="2"]').click(); pg2.wait_for_timeout(200)
    pg2.locator('#go').click(); pg2.wait_for_timeout(400)
    print('both-right verdict:',pg2.inner_text('#verdict h3')[:60])
    pg3=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg3.goto(P); pg3.wait_for_timeout(400)
    print('mobile h-scroll:',pg3.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg3.screenshot(path='build/b7f-mobile.png')
    b.close()
print('errors:',errs or 'none')
