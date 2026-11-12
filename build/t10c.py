from playwright.sync_api import sync_playwright
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/10-ai-tools.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    pg.on('pageerror',lambda e:print('PAGEERROR',e))
    pg.goto(P); pg.wait_for_timeout(600)
    print('locked before:',pg.evaluate("[...document.querySelectorAll('.node')].map(n=>n.classList.contains('locked'))"))
    for j,k in [(0,0),(1,1),(2,1),(3,0),(4,1),(5,0)]:
        pg.locator(f'[data-sort="0-{j}-{k}"]').click(); pg.wait_for_timeout(150)
    pg.wait_for_timeout(1200)
    print('locked after: ',pg.evaluate("[...document.querySelectorAll('.node')].map(n=>n.classList.contains('locked'))"))
    print('unlockedUpTo:',pg.evaluate("typeof unlockedUpTo!=='undefined'?unlockedUpTo:'n/a'"))
    print('picks present:',pg.evaluate("[...document.querySelectorAll('[data-pick]')].map(n=>n.dataset.pick).slice(0,8)"))
    b.close()
