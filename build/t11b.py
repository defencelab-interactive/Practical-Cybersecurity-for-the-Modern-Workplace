from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/11-data-classification.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':1050},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    print('counter at rest:',pg.inner_text('#trp-0'))
    pg.screenshot(path='build/c11-rest.png')
    pg.locator('[data-trace="0-0"]').dispatch_event('click'); pg.wait_for_timeout(500)
    print('after 1:',pg.inner_text('#trp-0'))
    pg.locator('[data-trace="0-1"]').dispatch_event('click'); pg.wait_for_timeout(500)
    print('after 2:',pg.inner_text('#trp-0'))
    pg.locator('[data-trace="0-2"]').dispatch_event('click'); pg.wait_for_timeout(900)
    print('after 3:',pg.inner_text('#trp-0'))
    print('feedback:',pg.locator('#trfb-0.show').count()==1)
    pg.evaluate("document.getElementById('trp-0').scrollIntoView({block:'center'})"); pg.wait_for_timeout(400)
    pg.screenshot(path='build/c11-counter.png')
    b.close()
print('errors:',errs or 'none')
