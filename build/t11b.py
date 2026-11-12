from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/11b-is-this-pii.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1150},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('items:',pg.locator('.it').count(),'| progress:',pg.inner_text('#pn'))
    print('done-box hidden at rest:',not pg.locator('#donebox').is_visible())
    print('escape artefacts:', '\\u' in pg.inner_text('body'))
    # answer all correctly: items 1 and 7 are "not personal data"
    correct=[1,0,1,1,1,1,1,0]
    for i,c in enumerate(correct):
        pg.locator(f'[data-a="{i}-{c}"]').click(); pg.wait_for_timeout(120)
    pg.wait_for_timeout(400)
    print('final:',pg.inner_text('#pn'))
    print('all right:',pg.locator('.it.right').count(),'| wrong:',pg.locator('.it.wrong').count())
    print('done-box shown:',pg.locator('#donebox').is_visible())
    print('explanations revealed:',pg.locator('.it.done .it-wi').count())
    # re-click does nothing
    pg.locator('.it').first.click(); pg.wait_for_timeout(150)
    print('score unchanged after stray click:',pg.inner_text('#pn'))
    src=open('bytes/11b-is-this-pii.html',encoding='utf-8').read()
    print('storage:', 'localStorage' in src or 'window.storage' in src, '| print:', 'window.print' in src)
    pg.screenshot(path='build/b11b.png')
    # wrong-answer path on a fresh load
    pg2=b.new_page(viewport={'width':1100,'height':900})
    pg2.goto(P); pg2.wait_for_timeout(400)
    pg2.locator('[data-a="5-0"]').click(); pg2.wait_for_timeout(300)
    print('wrong path verdict:',pg2.locator('#it-5 .verdict').inner_text(),'|',pg2.locator('#it-5 .tag').inner_text())
    pg3=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg3.goto(P); pg3.wait_for_timeout(400)
    print('mobile h-scroll:',pg3.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg3.screenshot(path='build/b11b-mobile.png')
    b.close()
print('errors:',errs or 'none')
