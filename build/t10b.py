from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/10-ai-tools.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    for j,k in [(0,0),(1,1),(2,1),(3,0),(4,1),(5,0)]:
        pg.locator(f'[data-sort="0-{j}-{k}"]').dispatch_event('click'); pg.wait_for_timeout(150)
    pg.wait_for_timeout(900)
    pg.locator('[data-opt="1"][data-j="1"]').dispatch_event('click'); pg.wait_for_timeout(1100)   # quiz node 1
    pg.locator('[data-exp="2"]').first.dispatch_event('click'); pg.wait_for_timeout(1100) # experience node 2
    pg.locator('[data-opt="3"][data-j="0"]').dispatch_event('click'); pg.wait_for_timeout(1100)   # predict node 3
    pg.locator('[data-opt="4"][data-j="0"]').dispatch_event('click'); pg.wait_for_timeout(1400)   # predict node 4
    print('end unlocked:',not pg.locator('.endcard').evaluate('e=>e.classList.contains("locked")'))
    print('xp:',pg.inner_text('#xp'))
    h=pg.evaluate("document.getElementById('track').scrollHeight")
    print('track height:',h,'px =',round(h/900,1),'screens')
    txt=pg.evaluate("document.getElementById('track').innerText")
    print('total words (incl. spots, closed deep dives):',len(txt.split()))
    deep=pg.evaluate("[...document.querySelectorAll('.more .more-in, .more-body, .more .mi')].map(n=>n.innerText).join(' ')")
    print('deep-dive words:',len(deep.split()))
    pg.locator('[data-check="5-0"]').dispatch_event('click');pg.locator('[data-check="5-2"]').dispatch_event('click');pg.wait_for_timeout(400)
    print('plan items:',pg.locator('#yourplan li').count())
    pg.evaluate("document.querySelector('.endcard').scrollIntoView()")
    pg.wait_for_timeout(300); pg.screenshot(path='build/c10-end.png')
    b.close()
print('errors:',errs or 'none')
