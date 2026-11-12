import io
# ---- 08b: drop the print promise ----
p='bytes/08b-lost-phone.html'
s=io.open(p,encoding='utf-8').read()
o="Ticks keep your place while you work through it. They live in this browser only — print this or save it as a PDF, because the day you need the right-hand tab is the day you do not have the phone."
n="Ticks keep your place while you work through it — they live in this browser only, so do not count on finding them again. The left-hand tab is the part to act on now: the day you need the right-hand one is the day you will not have this page either."
print(('ok  ' if o in s else 'MISS'),'08b'); s=s.replace(o,n,1)
io.open(p,'w',encoding='utf-8').write(s)

# ---- 02a: keep the card, handle a silent print failure ----
p2='bytes/02a-verification-card.html'
t=io.open(p2,encoding='utf-8').read()
o2=" sent anywhere. If you clear your browser data it goes with it — so print the card or photograph it once it's done."
n2=" sent anywhere. If you clear your browser data it goes with it — so photograph the card once it's done. That copy works on any phone, and it works when the page does not."
print(('ok  ' if o2 in t else 'MISS'),'02a note'); t=t.replace(o2,n2,1)
o3="Saved in this browser. <b>Print it, or photograph it</b> \\u2014 a card you cannot reach when your laptop is the problem isn\\u2019t much use."
n3="<b>Photograph it now.</b> A card you cannot reach when your laptop is the problem isn\\u2019t much use \\u2014 and if the Print button does nothing, the page is inside something that blocks printing, which is common."
print(('ok  ' if o3 in t else 'MISS'),'02a saveline'); t=t.replace(o3,n3,1)
io.open(p2,'w',encoding='utf-8').write(t)
