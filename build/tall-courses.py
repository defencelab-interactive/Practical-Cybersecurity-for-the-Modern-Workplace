from playwright.sync_api import sync_playwright
import glob,os
bad=0
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in sorted(glob.glob('courses/*.html'))+sorted(glob.glob('bytes/*.html')):
        pg=b.new_page(viewport={'width':1280,'height':900}); errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+os.path.abspath(f)); pg.wait_for_timeout(450)
        n=pg.locator('.node').count() or pg.locator('.acct,.step,.cat,.sh-row').count()
        hs=pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth")
        if errs or hs: bad+=1
        print(f'{os.path.basename(f):28} items={n:3} h-scroll={hs} errors={errs or "none"}')
        pg.close()
    b.close()
print('\nPROBLEMS:' if bad else '\nall clean')
