from playwright.sync_api import sync_playwright
import re
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/06-the-447-email.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(800)
    print('title:', pg.inner_text('h1'), '| nodes:', pg.locator('.node').count(), '| more:', pg.locator('.more').count())
    pg.locator('[data-pick="0-1"]').click(); pg.wait_for_timeout(1800)
    print('xp:', pg.inner_text('#xp'))
    pg.evaluate('document.querySelectorAll(".node").forEach(n=>{n.classList.remove("locked");n.classList.add("seen")})')
    pg.wait_for_timeout(300)
    for d,bt in zip(pg.locator('.date').all_inner_texts(), pg.locator('.beat').all_inner_texts()):
        print(f'  {d:22} | {bt}')
    pg.locator('[data-more]').first.click(); pg.wait_for_timeout(400)
    print('deep dive opens:', pg.locator('.more.open').count()>0)
    pg.locator('[data-fseg="3-1"]').click(); pg.wait_for_timeout(400)
    print('single flag panel:', pg.locator('.flag-one.show').count()==1, '| panels:', pg.locator('.flag-one').count())
    pg.locator('[data-fshow="3"]').click(); pg.wait_for_timeout(500)
    print('remainder compact:', pg.locator('.flags-rest .fr').count())
    print('checklist items:', pg.locator('[data-check]').count())
    print('end reachable without ticking:', not pg.locator('.endcard').evaluate('e=>e.classList.contains("locked")'))
    print('takeaways in end card:', pg.locator('.ec-t').count())
    pg.locator('[data-check="6-0"]').click(); pg.wait_for_timeout(400)
    print('plan live:', pg.locator('#yourplan li').count())
    b.close()
print('errors:', errs or 'none')
