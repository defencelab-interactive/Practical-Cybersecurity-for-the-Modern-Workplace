import io
p='bytes/04b-turn-on-mfa.html'
s=io.open(p,encoding='utf-8').read()
reps=[
# 1. honest lede, no "come back" promise
("Your accounts in the order that actually matters, with what each company calls the setting. Tick them off as you go — this browser remembers where you got to, so you can come back and finish.",
 "Your accounts in the order that actually matters, with what each company calls the setting. Work down it now if you can — and take it with you, because the ones you do not get to today are the ones that need the list."),
# 2. drop the add-your-own block entirely
("""  h+=`<div class="tier"><div class="tier-h"><span class="tier-n">+</span><span class="tier-t">Anything else you use</span></div>
    <div class="tier-w">Add the accounts this list does not know about — your own, your team's, the one you keep meaning to get to.</div>
    <div id="ownlist">${own.length?own.map(a=>rowHTML(a,true)).join(''):'<div class="empty">Nothing added yet. Whatever you type here is saved in this browser along with the ticks.</div>'}</div>
    <div class="own"><input id="ownin" placeholder="Account name" maxlength="46">
      <button id="ownadd">Add</button></div></div>`;
""","""  h+=`<div class="tier"><div class="tier-h"><span class="tier-n">+</span><span class="tier-t">Whatever this list does not know about</span></div>
    <div class="tier-w">Your own accounts, your team's tools, the one you keep meaning to get to. Same order applies: whatever holds the most, first. Write them on the printout.</div></div>`;
"""),
# 3. take-away bar
("""  <div class="prog"><span class="prog-n" id="pn">0 of 0 done</span><span class="prog-bar"><i id="pb"></i></span></div>""",
 """  <div class="prog"><span class="prog-n" id="pn">0 of 0 done</span><span class="prog-bar"><i id="pb"></i></span>
    <button class="print" id="print">Print or save as PDF</button></div>"""),
# 4. closing note: replace the storage paragraph with the take-it-with-you one
("<br><br><b>What gets saved.</b> Your ticks and anything you add stay in this browser on this device. They are not sent anywhere and will not follow you to your phone. Clearing site data clears them.",
 "<br><br><b>Take it with you.</b> The ticks are here to keep your place while you work down the list; they live in this browser on this device and nowhere else, so do not count on them. Anything you have not done by the time you close the tab should be on paper or in a PDF — that is what the button at the top is for."),
]
for a,b in reps:
    print(('ok  ' if a in s else 'MISS'),b[:56].replace('\n','/')); s=s.replace(a,b,1)

# 5. CSS: print button + print stylesheet
css = """.print{flex:none;border:1.5px solid var(--line);background:#fff;color:var(--tb);border-radius:10px;
  padding:9px 15px;font:700 12.5px var(--body);cursor:pointer;transition:all .15s;box-shadow:var(--sh)}
.print:hover{border-color:var(--acd);color:var(--acd)}
@media print{
  body{background:#fff}
  .wrap{max-width:none;padding:0}
  .chip,.print,.howto,.stale,.acct-go{display:none!important}
  .acct{break-inside:avoid;box-shadow:none;border-color:#bbb;padding:9px 12px;margin-bottom:5px}
  .acct.on{background:#fff}
  .tick{border-color:#555}
  .acct.on .tick{background:#fff;border-color:#555}
  .acct.on .tick svg{opacity:1;stroke:#000}
  .acct-n{font-size:14px}.acct-term{font-size:11px}
  .dec,.managed{break-inside:avoid;box-shadow:none;border-color:#bbb;padding:14px 16px}
  .tier{margin-top:18px;break-inside:avoid}
  h1{font-size:26px}.lede{font-size:13.5px}
  .prog{margin:14px 0 4px}.prog-bar{display:none}
  .printonly{display:block!important;margin-top:9px;border-top:1px dashed #bbb;padding-top:9px}
  .printonly i{display:block;height:17px;border-bottom:1px solid #ccc;margin-bottom:7px}
}
.printonly{display:none}
"""
s=s.replace(".tier{margin-top:30px}", css+".tier{margin-top:30px}",1)

# 6. write-your-own lines appear on the printout
s=s.replace("""Same order applies: whatever holds the most, first. Write them on the printout.</div></div>`;""",
"""Same order applies: whatever holds the most, first. Write them on the printout.</div>
    <div class="printonly"><i></i><i></i><i></i><i></i></div></div>`;""",1)

# 7. print handler, and drop the now-dead own-account code
s=s.replace("""  if(e.target.id==='ownadd'){addOwn(); return;}""",
            """  if(e.target.id==='print'){window.print(); return;}""",1)
s=s.replace("""document.addEventListener('keydown',e=>{
  if(e.key==='Enter'&&e.target.id==='ownin'){e.preventDefault();addOwn();}
});
function addOwn(){
  const i=document.getElementById('ownin'); if(!i)return;
  const v=i.value.trim(); if(!v)return;
  own.push({id:'own-'+Date.now().toString(36),n:v,term:'',url:''});
  i.value=''; render(); save();
  const ni=document.getElementById('ownin'); if(ni)ni.focus();
}
""","",1)
io.open(p,'w',encoding='utf-8').write(s)
