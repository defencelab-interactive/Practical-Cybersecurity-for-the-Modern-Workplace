from playwright.sync_api import sync_playwright
import math, collections
errs=[]
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/04a-build-a-passphrase.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':1100},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(600)
    print('title:',pg.title())
    print('wordlist length:',pg.evaluate("WORDS.length"),'| unique:',pg.evaluate("new Set(WORDS).size"))
    print('bits per word:',pg.evaluate("BITS_PER_WORD"))
    print('phrase:',pg.inner_text('#phrase'))
    print('bits shown:',pg.inner_text('#bits'),'| meta:',pg.inner_text('#guesses'))
    # word-count control
    for n in [4,6,7]:
        pg.locator(f'[data-w="{n}"]').click(); pg.wait_for_timeout(200)
        ph=pg.inner_text('#phrase'); bits=pg.inner_text('#bits')
        got=len(ph.split('-'))
        print(f'  {n} words -> parts={got} bits={bits}', 'OK' if got==n and bits==str(n*9) else 'MISMATCH')
    # separator
    pg.locator('[data-s="."]').click(); pg.wait_for_timeout(200)
    print('separator dot:', '.' in pg.inner_text('#phrase'), '| bits unchanged:', pg.inner_text('#bits'))
    pg.locator('[data-s=" "]').click(); pg.wait_for_timeout(200)
    print('separator space:', ' ' in pg.inner_text('#phrase'))
    pg.locator('[data-s="-"]').click(); pg.wait_for_timeout(150)
    # randomness: 400 draws, check spread and no repeats within a phrase
    vals=pg.evaluate("""() => {const out=[]; for(let i=0;i<400;i++){ document.getElementById('again').click();
        out.push(document.getElementById('phrase').textContent);} return out;}""")
    allw=[w for v in vals for w in v.split('-')]
    c=collections.Counter(allw)
    print('draws:',len(vals),'| distinct phrases:',len(set(vals)),'| distinct words seen:',len(c))
    print('most common word count:',c.most_common(1)[0][1],'(expect ~',round(len(allw)/512,1),'if uniform)')
    print('bars:',pg.locator('.bar').count(),'| my bar highlighted:',pg.locator('.bar.me').count()==1)
    src=open(p if False else 'bytes/04a-build-a-passphrase.html',encoding='utf-8').read()
    print('uses crypto:', 'crypto.getRandomValues' in src, '| Math.random:', 'Math.random' in src)
    print('crack-time claims:', any(x in src for x in ['years to crack','centuries','seconds to crack']))
    print('storage:', 'localStorage' in src, '| print:', 'window.print' in src)
    pg.screenshot(path='build/b4a.png')
    pg2=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg2.goto(P); pg2.wait_for_timeout(500)
    print('mobile h-scroll:',pg2.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
    pg2.screenshot(path='build/b4a-mobile.png')
    b.close()
print('errors:',errs or 'none')
