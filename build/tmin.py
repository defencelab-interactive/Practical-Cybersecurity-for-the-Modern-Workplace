from playwright.sync_api import sync_playwright
errs=[]
root='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/build/03-min.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(root); pg.wait_for_timeout(800)
    pg.locator('[data-aud="0-0"]').click(); pg.wait_for_timeout(120)
    pg.locator('[data-audgo="0"]').click(); pg.wait_for_timeout(2200)
    print('node1 open:', not pg.locator('.node').nth(1).evaluate('e=>e.classList.contains("locked")'))
    pg.wait_for_timeout(900)
    print('node2 chain-unlocked:', not pg.locator('.node').nth(2).evaluate('e=>e.classList.contains("locked")'))
    pg.locator('.spot-trigger').first.click(); pg.wait_for_timeout(350)
    pg.locator('[data-opt]').nth(1).click(); pg.wait_for_timeout(2000)
    pg.locator('[data-more]').first.click(); pg.wait_for_timeout(400)
    print('deep dive opens:', pg.locator('.more.open').count()>0)
    pg.locator('.spot-trigger').nth(1).click(); pg.wait_for_timeout(350)
    pg.locator('[data-opt]').nth(4).click(); pg.wait_for_timeout(2000)
    for fi in range(9):
        pg.locator(f'[data-fseg="4-{fi}"]').click(); pg.wait_for_timeout(70)
    pg.wait_for_timeout(1200)
    print('checklist node open:', not pg.locator('.node').nth(5).evaluate('e=>e.classList.contains("locked")'))
    print('end reachable:', not pg.locator('.endcard').evaluate('e=>e.classList.contains("locked")'))
    for j in range(3):
        pg.locator(f'[data-check="5-{j}"]').click(); pg.wait_for_timeout(120)
    pg.wait_for_timeout(400)
    pg.locator('.endcard').scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    print('plan items:', pg.locator('#yourplan li').count(), '| takeaways:', pg.locator('.ec-t').count())
    pg.screenshot(path='build/min-end.png')
    b.close()
print('errors:', errs or 'none')
