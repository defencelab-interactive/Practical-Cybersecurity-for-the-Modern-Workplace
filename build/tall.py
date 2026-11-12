from playwright.sync_api import sync_playwright
B='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/'
checks=[('07b-home-wifi.html','.step','.step.on','click','.step .s-top'),
        ('08b-lost-phone.html','.step','.step.done','click','.step .s-top')]
with sync_playwright() as p:
    b=p.chromium.launch()
    for f,sel,onsel,_,clicksel in checks:
        pg=b.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(B+f); pg.wait_for_timeout(500)
        pg.locator(clicksel).first.click(); pg.wait_for_timeout(400)
        before=pg.locator(onsel).count()
        pg.reload(); pg.wait_for_timeout(700)
        after=pg.locator(onsel).count()
        print(f'{f:28} before={before} after_reload={after}  {"OK" if after==before and before>0 else "FAIL"}  errors:{errs or "none"}')
        pg.close()
    # 02a form
    pg=b.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'02a-verification-card.html'); pg.wait_for_timeout(500)
    ins=pg.locator('input.inp')
    print('02a inputs:',ins.count())
    if ins.count():
        pg.locator('.ctx').first.click(); pg.wait_for_timeout(400)
        i2=pg.locator('input.inp').first
        i2.fill('Dana in finance'); i2.dispatch_event('input'); pg.wait_for_timeout(600)
        pg.reload(); pg.wait_for_timeout(800)
        v=pg.locator('input.inp').first.input_value() if pg.locator('input.inp').count() else ''
        print('02a after reload value:',repr(v),'OK' if 'Dana' in v else 'FAIL')
    print('02a errors:',errs or 'none')
    b.close()
