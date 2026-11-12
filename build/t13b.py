from playwright.sync_api import sync_playwright
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/courses/13-incident-response.html'
def seq(pg): return pg.evaluate("[...document.getElementById('orp-0').children].map(c=>+c.dataset.oritem)")
def nums(pg): return pg.evaluate("[...document.querySelectorAll('#orp-0 .or-n')].map(n=>n.textContent)")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(700)
    print('start seq:',seq(pg),'numbers:',nums(pg))
    print('first up disabled:',pg.locator('#orp-0 .or-c').first.locator('[aria-label="Move up"]').is_disabled())
    print('last down disabled:',pg.locator('#orp-0 .or-c').last.locator('[aria-label="Move down"]').is_disabled())
    # arrows
    pg.locator('#orp-0 .or-c').nth(1).locator('[aria-label="Move up"]').click(); pg.wait_for_timeout(300)
    print('after arrow up on row2:',seq(pg),'numbers:',nums(pg))
    # drag: grab row 3 grip and drop at top
    rows=pg.locator('#orp-0 .or-c')
    g=rows.nth(2).locator('.or-grip'); gb=g.bounding_box(); tb=rows.nth(0).bounding_box()
    pg.mouse.move(gb['x']+gb['width']/2, gb['y']+gb['height']/2)
    pg.mouse.down()
    pg.mouse.move(gb['x']+gb['width']/2, tb['y']+4, steps=12)
    pg.wait_for_timeout(150); pg.mouse.up(); pg.wait_for_timeout(350)
    print('after drag to top:',seq(pg),'numbers:',nums(pg))
    pg.screenshot(path='build/c13-drag.png')
    # set correct order 1,3,0,2 via arrows then check
    pg.evaluate("""() => {const pool=document.getElementById('orp-0');
      [1,3,0,2].forEach(idx=>{const el=[...pool.children].find(c=>+c.dataset.oritem===idx);pool.appendChild(el);});
      orRenumber(0);}""")
    pg.wait_for_timeout(200); print('forced correct:',seq(pg))
    pg.locator('[data-orcheck="0"]').click(); pg.wait_for_timeout(800)
    print('verdict:',pg.inner_text('#orn-0'),'| right:',pg.locator('.or-c.right').count())
    print('grips hidden after check:',not pg.locator('#orp-0 .or-grip').first.is_visible())
    print('feedback:',pg.locator('#orfb-0.show').count()==1,'| xp:',pg.inner_text('#xp'))
    pg.locator('[data-ordreset="0"]').click(); pg.wait_for_timeout(400)
    print('after retry — check button back:',pg.locator('[data-orcheck="0"]').count()==1,'| grips back:',pg.locator('#orp-0 .or-grip').first.is_visible())
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2,has_touch=True,is_mobile=True)
    pg2.goto(P); pg2.wait_for_timeout(700)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    print('mobile arrows visible:',pg2.locator('#orp-0 .or-a').first.is_visible())
    pg2.locator('#orp-0 .or-c').nth(3).locator('[aria-label="Move up"]').tap(); pg2.wait_for_timeout(300)
    print('mobile arrow works:',pg2.evaluate("[...document.getElementById('orp-0').children].map(c=>+c.dataset.oritem)"))
    pg2.screenshot(path='build/c13-drag-mobile.png')
    b.close()
print('errors:',errs or 'none')
