from playwright.sync_api import sync_playwright
P='file:///home/claude/practical-cybersecurity-for-the-modern-workplace/bytes/04b-turn-on-mfa.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.goto(P); pg.wait_for_timeout(500)
    print('window.storage exists?', pg.evaluate("typeof window.storage"))
    pg.locator('[data-tick="google"]').click(); pg.wait_for_timeout(300)
    pg.fill('#ownin','Company VPN'); pg.locator('#ownadd').click(); pg.wait_for_timeout(300)
    print('before reload:', pg.inner_text('#pn'))
    pg.reload(); pg.wait_for_timeout(600)
    print('AFTER RELOAD:', pg.inner_text('#pn'), '| own rows:', pg.locator('#ownlist .acct').count())
    b.close()
