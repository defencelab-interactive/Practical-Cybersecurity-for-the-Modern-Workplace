from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/03-physical-security-min.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':950})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    pg.evaluate('document.querySelectorAll(".node").forEach(n=>{n.classList.remove("locked");n.classList.add("seen")})')
    pg.wait_for_timeout(300)
    print('duplicate hint gone:', pg.locator('.flags-hint').count()==0)
    print('counter start:', pg.inner_text('#fc-4'))
    pg.locator('[data-fseg="4-1"]').click(); pg.wait_for_timeout(400)
    print('after 1 click -> counter:', pg.inner_text('#fc-4'))
    print('single panel shown:', pg.locator('#fone-4.show').count()==1, '| text:', pg.inner_text('#fone-4')[:50])
    pg.locator('[data-fseg="4-6"]').click(); pg.wait_for_timeout(400)
    print('decoy replaces panel (not stacks):', pg.locator('#fone-4.decoy').count()==1)
    print('panels on page (should stay 1):', pg.locator('.flag-one').count())
    pg.locator('[data-fshow="4"]').click(); pg.wait_for_timeout(500)
    print('remaining listed compactly:', pg.locator('.flags-rest .fr').count())
    print('fb shown:', pg.locator('#ffb-4.show').count()==1)
    pg.locator('.flags-spot').scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    pg.screenshot(path='build/flags-new.png', full_page=False)
    b.close()
print('errors:', errs or 'none')
