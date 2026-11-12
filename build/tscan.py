from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/03-physical-security-min.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':950})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    pg.evaluate('document.querySelectorAll(".node").forEach(n=>{n.classList.remove("locked");n.classList.add("seen")})')
    pg.wait_for_timeout(300)
    print('items:', pg.locator('.sc-i').count(), '| old mail markup gone:', pg.locator('.flags-spot').count()==0)
    print('counter:', pg.inner_text('#sn-4'))
    pg.locator('[data-scan="4-1"]').click(); pg.wait_for_timeout(450)
    print('after flag click -> counter:', pg.inner_text('#sn-4'), '| marked:', pg.inner_text('#sc-4-1 .sc-m'))
    print('explanation open under item:', pg.locator('#sc-4-1 .sc-w').bounding_box()['height']>20)
    pg.locator('[data-scan="4-6"]').click(); pg.wait_for_timeout(400)
    print('decoy marked:', pg.inner_text('#sc-4-6 .sc-m'), '| counter unchanged:', pg.inner_text('#sn-4'))
    pg.locator('.scan-spot').scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    pg.screenshot(path='build/scan-mid.png')
    pg.locator('[data-scango="4"]').click(); pg.wait_for_timeout(600)
    print('fb shown:', pg.locator('#ffb-4.show').count()==1)
    print('remaining revealed:', pg.locator('.sc-i.left').count())
    pg.screenshot(path='build/scan-done.png')
    b.close()
print('errors:', errs or 'none')
