from playwright.sync_api import sync_playwright
B='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/'
with sync_playwright() as p:
    b=p.chromium.launch()
    # 08b: open the tab that holds .step first
    pg=b.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'08b-lost-phone.html'); pg.wait_for_timeout(500)
    tabs=pg.locator('.tab'); print('08b tabs:',tabs.count())
    for i in range(tabs.count()):
        tabs.nth(i).click(); pg.wait_for_timeout(300)
        vis=pg.locator('.step .s-top:visible').count()
        if vis: print('  steps visible on tab',i,':',vis); break
    pg.locator('.step .s-top:visible').first.click(); pg.wait_for_timeout(400)
    before=pg.locator('.step.done').count()
    pg.reload(); pg.wait_for_timeout(800)
    after=pg.locator('.step.done').count()
    print(f'08b-lost-phone  before={before} after_reload={after}  {"OK" if after==before and before>0 else "FAIL"}  errors:{errs or "none"}')
    pg.close()
    # 02a
    pg=b.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'02a-verification-card.html'); pg.wait_for_timeout(500)
    print('02a ctx options:',pg.locator('.ctx').count(),'| inputs now:',pg.locator('input').count())
    if pg.locator('.ctx').count():
        pg.locator('.ctx').first.click(); pg.wait_for_timeout(500)
    ins=pg.locator('input:visible'); print('02a visible inputs:',ins.count())
    if ins.count():
        ins.first.fill('Dana in finance'); ins.first.dispatch_event('input')
        ins.first.dispatch_event('change'); pg.wait_for_timeout(700)
        pg.reload(); pg.wait_for_timeout(900)
        if pg.locator('.ctx').count() and pg.locator('input:visible').count()==0:
            pg.locator('.ctx').first.click(); pg.wait_for_timeout(500)
        v=pg.locator('input:visible').first.input_value() if pg.locator('input:visible').count() else ''
        print('02a after reload:',repr(v),'OK' if 'Dana' in v else 'FAIL')
    print('02a errors:',errs or 'none')
    b.close()
