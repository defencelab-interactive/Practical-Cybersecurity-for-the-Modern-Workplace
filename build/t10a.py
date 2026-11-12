from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/10a-anonymise-prompt.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1150},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('loads with example:', len(pg.locator('#in').input_value())>50)
    print('auto tags found:',pg.locator('.t-auto').count())
    print('kinds:',[t.strip() for t in pg.locator('.f').all_inner_texts()])
    out=pg.inner_text('#out')
    for leak in ['marcus.webb@','+44 7700','18,400','4471982','srv-fin-02','14/09/2026']:
        print(f'  leaked {leak!r}:', leak in out)
    # manual marking cycles and applies to every occurrence
    words=pg.locator('#out [data-word]')
    print('clickable words:',words.count())
    tgt=pg.locator('#out [data-word="hartwell"]').first
    print('Hartwell present:', tgt.count()>0 if hasattr(tgt,'count') else True)
    for expect in ['[NAME]','[COMPANY]','[PROJECT]']:
        pg.locator('#out [data-word="hartwell"]').first.click(); pg.wait_for_timeout(180)
        got=pg.locator('#out [data-word="hartwell"]').first.inner_text()
        n=pg.locator('#out [data-word="hartwell"]').count()
        print(f'  click -> {got} (all {n} occurrences)', 'OK' if got==expect else 'MISMATCH')
    pg.locator('#out [data-word="hartwell"]').first.click(); pg.wait_for_timeout(180)
    print('  fourth click unmarks:', pg.locator('#out [data-word="hartwell"]').first.inner_text())
    # empty state
    pg.locator('#clear').click(); pg.wait_for_timeout(250)
    print('empty state:',pg.inner_text('#out')[:48])
    pg.locator('#example').click(); pg.wait_for_timeout(250)
    print('reload example ok:',pg.locator('.t-auto').count()>0)
    src=open('bytes/10a-anonymise-prompt.html',encoding='utf-8').read()
    print('storage:', 'localStorage' in src or 'window.storage' in src, '| print:', 'window.print' in src, '| network calls:', 'fetch(' in src)
    pg.screenshot(path='build/b10a.png')
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(500)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg2.screenshot(path='build/b10a-mobile.png')
    b.close()
print('errors:',errs or 'none')
