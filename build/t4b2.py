from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/04b-turn-on-mfa.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1150},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(500); pg.evaluate("localStorage.clear()")
    pg.reload(); pg.wait_for_timeout(600)
    print('accounts:',pg.locator('.acct').count(),'| tiers:',pg.locator('.tier').count())
    print('print button:',pg.locator('#print').count(),'| own input gone:',pg.locator('#ownin').count()==0)
    pg.locator('[data-tick="google"]').click(); pg.wait_for_timeout(250)
    print('tick works:',pg.inner_text('#pn'))
    pg.reload(); pg.wait_for_timeout(600)
    print('tick survives reload:',pg.inner_text('#pn'))
    # print layout
    pg.emulate_media(media='print'); pg.wait_for_timeout(300)
    print('hidden in print - howto:',pg.locator('.howto').is_visible(),'| links:',pg.locator('a.acct-go').first.is_visible())
    print('write-in lines visible in print:',pg.locator('.printonly').first.is_visible())
    pg.screenshot(path='build/b4b-print.png',full_page=False)
    pg.emulate_media(media='screen'); pg.wait_for_timeout(200)
    pg.screenshot(path='build/b4b-final.png')
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(600)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    b.close()
print('errors:',errs or 'none')
