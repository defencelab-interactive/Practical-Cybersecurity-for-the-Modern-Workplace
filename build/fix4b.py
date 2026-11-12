import io
p='bytes/04b-turn-on-mfa.html'
s=io.open(p,encoding='utf-8').read()
reps=[
# row rendering: instruction in the line, button only where a link is verified
("""  const go = a.url
    ? `<a class="acct-go" href="${a.url}" target="_blank" rel="noopener">Open guide</a>`
    : `<span class="acct-go">Search their help</span>`;
  return `<div class="acct" data-id="${a.id}">
    <button class="tick" data-tick="${a.id}" aria-label="Mark ${a.n} done">${TICK}</button>
    <div class="acct-b"><div class="acct-n">${a.n}</div>
      <div class="acct-term">${isOwn?'Search: <b>two-factor authentication</b>':'Their term: <b>'+a.term+'</b>'}</div></div>
    ${isOwn?'<button class="acct-x" data-rm="'+a.id+'" aria-label="Remove">&times;</button>':go}
  </div>`;""",
 """  let line;
  if(isOwn) line='In its settings, look for <b>two-factor authentication</b> or <b>two-step verification</b>';
  else if(a.url) line='They call it <b>'+a.term+'</b>';
  else line='In their own help centre, search <b>'+a.term+'</b>';
  const go = a.url
    ? `<a class="acct-go" href="${a.url}" target="_blank" rel="noopener">Open their guide</a>` : '';
  return `<div class="acct${a.url?'':' nolink'}" data-id="${a.id}">
    <button class="tick" data-tick="${a.id}" aria-label="Mark ${a.n} done">${TICK}</button>
    <div class="acct-b"><div class="acct-n">${a.n}</div>
      <div class="acct-term">${line}</div></div>
    ${isOwn?'<button class="acct-x" data-rm="'+a.id+'" aria-label="Remove">&times;</button>':go}
  </div>`;"""),
# empty state for the own list
("""    <div id="ownlist">${own.map(a=>rowHTML(a,true)).join('')}</div>""",
 """    <div id="ownlist">${own.length?own.map(a=>rowHTML(a,true)).join(''):'<div class="empty">Nothing added yet. Whatever you type here is saved in this browser along with the ticks.</div>'}</div>"""),
# honest lede
("Your accounts in the order that actually matters, with what each company calls the setting. Tick them off as you go — this page remembers.",
 "Your accounts in the order that actually matters, with what each company calls the setting. Tick them off as you go — this browser remembers where you got to, so you can come back and finish."),
# CSS: empty state + no-link row
(".own{display:flex;gap:9px;margin-top:11px}",
 ".empty{font-size:14px;line-height:1.6;color:var(--mu);padding:3px 2px 2px}\n"
 ".acct.nolink .acct-term b{color:var(--acd)}\n"
 ".own{display:flex;gap:9px;margin-top:11px}"),
# explain the asymmetry above the list rather than per row
("""  <div class="prog"><span class="prog-n" id="pn">0 of 0 done</span><span class="prog-bar"><i id="pb"></i></span></div>""",
 """  <div class="prog"><span class="prog-n" id="pn">0 of 0 done</span><span class="prog-bar"><i id="pb"></i></span></div>
  <div class="howto">Each account shows the company’s own name for the setting — that is the phrase that finds the current instructions. Where there is a button, the link to their guide was confirmed. Where there is not, the term is right but the address was not confirmed, so search it on the company’s own site rather than trusting a stranger’s walkthrough.</div>"""),
(".tier{margin-top:30px}",
 ".howto{font-size:14px;line-height:1.65;color:var(--tb);background:rgba(78,124,168,.06);border:1.5px solid rgba(78,124,168,.2);"
 "border-radius:13px;padding:14px 17px;margin-top:14px;max-width:none}\n.tier{margin-top:30px}"),
# the bottom note no longer needs to carry the same explanation
("<b>On the links.</b> Menu paths and screenshots go out of date within months, so this page does not use them. Each account shows <b>the company's own term</b> — which is what finds the current instructions in their help search — and links straight to the vendor's own page where that link was confirmed. Where it says <i>search their help</i>, the term is right and the link was not confirmed, so look it up on the company's own site rather than trusting a third-party walkthrough.\n    <br><br>Links confirmed November 2026. If one has moved since, search the term on the company's own help site; the term changes far less often than the address.",
 "<b>Why there are no screenshots.</b> Menu paths and screenshots go out of date within months — vendors move things, the web and the app differ, and on a managed account the option may not be where anyone else sees it. Terms change far more slowly than addresses, so this page gives you the term.\n    <br><br>Links confirmed November 2026. If one has moved since, search the term on the company’s own help site.\n    <br><br><b>What gets saved.</b> Your ticks and anything you add stay in this browser on this device. They are not sent anywhere and will not follow you to your phone. Clearing site data clears them."),
]
for a,b in reps:
    print(('ok  ' if a in s else 'MISS'),b[:58].replace('\n','/')); s=s.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(s)
