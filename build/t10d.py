from playwright.sync_api import sync_playwright
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/10-ai-tools.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=2)
    pg.goto(P); pg.wait_for_timeout(700)
    pg.screenshot(path='build/c10-sort-start.png')
    for j,k in [(0,0),(1,1),(2,1)]:
        pg.locator(f'[data-sort="0-{j}-{k}"]').dispatch_event('click'); pg.wait_for_timeout(200)
    pg.wait_for_timeout(500); pg.screenshot(path='build/c10-sort-mid.png')
    for j,k in [(3,0),(4,0),(5,0)]:
        pg.locator(f'[data-sort="0-{j}-{k}"]').dispatch_event('click'); pg.wait_for_timeout(200)
    pg.wait_for_timeout(800)
    pg.evaluate("document.getElementById('sofb-0').scrollIntoView({block:'center'})"); pg.wait_for_timeout(400)
    pg.screenshot(path='build/c10-sort-done.png')
    b.close()
