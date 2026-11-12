import io,re
FILES=['02a-verification-card','04b-turn-on-mfa','06b-link-inspector','07b-home-wifi','08b-lost-phone']
for f in FILES:
    p='bytes/'+f+'.html'
    s=io.open(p,encoding='utf-8').read()
    before=s
    # one column width everywhere
    s=re.sub(r"\.wrap\{max-width:(?:860|900|920)px;margin:0 auto;padding:40px 32px 80px\}",
             ".wrap{max-width:1000px;margin:0 auto;padding:40px 36px 80px}", s)
    # drop reading-measure caps so every block shares the column's edges
    s=re.sub(r";?max-width:\d+ch", "", s)
    # nudge the small prose up a notch now that lines are longer
    s=s.replace(".tier-w{font-size:14.5px;line-height:1.6",".tier-w{font-size:15px;line-height:1.62")
    s=s.replace(".sub{font-size:14.5px;line-height:1.6",".sub{font-size:15px;line-height:1.62")
    s=s.replace(".stale{margin-top:34px;border-top:1px solid var(--line);padding-top:17px;font-size:13px;line-height:1.65",
                ".stale{margin-top:34px;border-top:1px solid var(--line);padding-top:17px;font-size:13.5px;line-height:1.7")
    io.open(p,'w',encoding='utf-8').write(s)
    print(('changed' if s!=before else 'no-op  '), f)
