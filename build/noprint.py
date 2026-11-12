import io
p='bytes/04b-turn-on-mfa.html'
s=io.open(p,encoding='utf-8').read()
reps=[
# remove the button
("""<span class="prog-bar"><i id="pb"></i></span>
    <button class="print" id="print">Print or save as PDF</button></div>""",
 """<span class="prog-bar"><i id="pb"></i></span></div>"""),
("""  if(e.target.id==='print'){window.print(); return;}\n""",""),
(".print{flex:none;border:1.5px solid var(--line);background:#fff;color:var(--tb);border-radius:10px;\n  padding:9px 15px;font:700 12.5px var(--body);cursor:pointer;transition:all .15s;box-shadow:var(--sh)}\n.print:hover{border-color:var(--acd);color:var(--acd)}\n",""),
("  .chip,.print,.howto,.stale,.acct-go{display:none!important}","  .chip,.howto,.stale,.acct-go{display:none!important}"),
# lede: do it now, no takeaway promise
("Your accounts in the order that actually matters, with what each company calls the setting. Work down it now if you can — and take it with you, because the ones you do not get to today are the ones that need the list.",
 "Your accounts in the order that actually matters, with what each company calls the setting. The first three are the ones worth doing before you close this — they take about a minute each, and everything below them depends on them."),
# own-accounts section: no printout reference
("Your own accounts, your team's tools, the one you keep meaning to get to. Same order applies: whatever holds the most, first. Write them on the printout.",
 "Your own accounts, your team's tools, the one you keep meaning to get to. Same order applies: whatever opens the most, first — and anything that can reset another account counts as opening it."),
# drop the write-in lines (they only existed for the printout)
("""    <div class="printonly"><i></i><i></i><i></i><i></i></div></div>`;""","""</div>`;"""),
("  .printonly{display:block!important;margin-top:9px;border-top:1px dashed #bbb;padding-top:9px}\n  .printonly i{display:block;height:17px;border-bottom:1px solid #ccc;margin-bottom:7px}\n",""),
(".printonly{display:none}\n",""),
# closing note
("<br><br><b>Take it with you.</b> The ticks are here to keep your place while you work down the list; they live in this browser on this device and nowhere else, so do not count on them. Anything you have not done by the time you close the tab should be on paper or in a PDF — that is what the button at the top is for.",
 "<br><br><b>The ticks.</b> They keep your place while you work down the list, and that is all they do — they live in this browser on this device, so do not count on finding them again. Nothing here is worth coming back for: the value is in the three at the top, done now."),
]
for a,b in reps:
    print(('ok  ' if a in s else 'MISS'),(b[:52] or '[removed]').replace('\n','/')); s=s.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(s)
