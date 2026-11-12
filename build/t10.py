from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/10-ai-tools.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    print('title:',pg.inner_text('h1'),'| nodes:',pg.locator('.node').count(),'| deep dives:',pg.locator('.more').count())
    # sort opening
    print('sort items:',pg.locator('[id^="so-0-"]').count())
    for j,k in [(0,0),(1,1),(2,1),(3,0),(4,1),(5,0)]:
        pg.locator(f'[data-sort="0-{j}-{k}"]').click(); pg.wait_for_timeout(180)
    pg.wait_for_timeout(600)
    print('progress:',pg.inner_text('#sop-0'))
    print('all right:',pg.locator('[id^="so-0-"].right').count(),'of 6')
    print('feedback shown:',pg.locator('#sofb-0.show').count()==1)
    print('xp after sort:',pg.inner_text('#xp'))
    pg.evaluate('document.querySelectorAll(".node").forEach(n=>{n.classList.remove("locked");n.classList.add("seen")})')
    pg.wait_for_timeout(250)
    for d,bt in zip(pg.locator('.date').all_inner_texts(),pg.locator('.beat').all_inner_texts()):
        print(f'  {d:20} | {bt}')
    pg.locator('[data-more]').first.click(); pg.wait_for_timeout(400)
    print('deep dive opens:',pg.locator('.more.open').count()>0)
    print('checklist items:',pg.locator('[data-check]').count())
    print('takeaways:',pg.locator('.ec-t').count(),'| sources block:',pg.locator('.ec-src').count())
    print('end not gated:',not pg.locator('.endcard').evaluate('e=>e.classList.contains("locked")'))
    pg.locator('[data-check="5-0"]').click(); pg.wait_for_timeout(400)
    print('plan live:',pg.locator('#yourplan li').count())
    # word count
    import re
    txt=pg.evaluate("[...document.querySelectorAll('.node .body')].map(n=>n.innerText).join(' ')")
    print('base words:',len(txt.split()))
    pg.screenshot(path='build/c10-open.png',full_page=False)
    # mobile
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(700)
    w=pg2.evaluate("document.querySelector('.node .body').getBoundingClientRect().width")
    print('mobile body width:',round(w),'| h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg2.screenshot(path='build/c10-mobile.png')
    b.close()
print('errors:',errs or 'none')
