from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/13-incident-response.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    print('title:',pg.inner_text('h1'),'| nodes:',pg.locator('.node').count(),'| deep dives:',pg.locator('.more').count())
    print('order items:',pg.locator('[data-ord]').count(),'| hint:',pg.inner_text('#orn-0'))
    pg.screenshot(path='build/c13-order.png')
    # correct order is items 1,3,0,2
    for j in [1,3,0,2]:
        pg.locator(f'[data-ord="0-{j}"]').click(); pg.wait_for_timeout(250)
    pg.wait_for_timeout(700)
    print('verdict:',pg.inner_text('#orn-0'))
    print('right:',pg.locator('.or-i.right').count(),'wrong:',pg.locator('.or-i.wrong').count())
    print('feedback:',pg.locator('#orfb-0.show').count()==1,'| xp:',pg.inner_text('#xp'))
    pg.evaluate("document.querySelector('.or-pool').scrollIntoView({block:'start'})"); pg.wait_for_timeout(400)
    pg.screenshot(path='build/c13-order-done.png')
    # reset path
    pg.locator('[data-ordreset="0"]').click(); pg.wait_for_timeout(400)
    print('after reset, picked:',pg.locator('.or-i.picked').count(),'| hint:',pg.inner_text('#orn-0'))
    for j in [0,1,2,3]:
        pg.locator(f'[data-ord="0-{j}"]').click(); pg.wait_for_timeout(150)
    pg.wait_for_timeout(600)
    print('wrong-order verdict:',pg.inner_text('#orn-0'))
    pg.locator('[data-opt="1"][data-j="0"]').dispatch_event('click'); pg.wait_for_timeout(1100)
    pg.locator('[data-opt="2"][data-j="0"]').dispatch_event('click'); pg.wait_for_timeout(1100)
    pg.locator('[data-exp="3"]').first.dispatch_event('click'); pg.wait_for_timeout(1400)
    print('end unlocked:',not pg.locator('.endcard').evaluate('e=>e.classList.contains("locked")'))
    h=pg.evaluate("document.getElementById('track').scrollHeight"); print('height:',round(h/1000,1),'screens')
    print('takeaways:',pg.locator('.ec-t').count(),'| sources:',pg.locator('.ec-src').count())
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(600)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg2.screenshot(path='build/c13-mobile.png')
    b.close()
print('errors:',errs or 'none')
