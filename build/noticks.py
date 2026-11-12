import io
p='bytes/04b-turn-on-mfa.html'
s=io.open(p,encoding='utf-8').read()

# 1. replace everything from <script> to </script> with a static renderer
a=s.index('<script>\nconst TICK=')
b=s.index('</script>',a)
data=s[s.index('const TIERS=['):s.index('];',s.index('const TIERS=['))+2]
new_script = "<script>\n"+data+"""

function rowHTML(a){
  const line = a.line ? a.line
             : a.url ? 'They call it <b>'+a.term+'</b>'
                     : 'In their own help centre, search <b>'+a.term+'</b>';
  const go = a.url
    ? `<a class="acct-go" href="${a.url}" target="_blank" rel="noopener">Open their guide</a>` : '';
  return `<div class="acct${a.url?'':' nolink'}">
    <div class="acct-b"><div class="acct-n">${a.n}</div>
      <div class="acct-term">${line}</div></div>
    ${go}
  </div>`;
}

let h='';
TIERS.forEach(t=>{
  h+=`<div class="tier"><div class="tier-h"><span class="tier-n">${t.n}</span><span class="tier-t">${t.t}</span></div>
    <div class="tier-w">${t.w}</div>${t.items.map(rowHTML).join('')}</div>`;
});
h+=`<div class="tier"><div class="tier-h"><span class="tier-n">+</span><span class="tier-t">Whatever this list does not know about</span></div>
  <div class="tier-w">Your own accounts, your team's tools, the one you keep meaning to get to. Same order applies: whatever opens the most, first \\u2014 and anything that can reset another account counts as opening it.</div></div>`;
document.getElementById('tiers').innerHTML=h;
"""
s=s[:a]+new_script+s[b:]

# 2. strip the progress bar markup
o="""  <div class="prog"><span class="prog-n" id="pn">0 of 0 done</span><span class="prog-bar"><i id="pb"></i></span></div>
"""
print(('ok  ' if o in s else 'MISS'),'prog markup'); s=s.replace(o,"",1)

# 3. strip tick + progress CSS
for frag in [
"/* progress */\n.prog{display:flex;align-items:center;gap:13px;margin:28px 0 8px}\n.prog-n{font:700 13px var(--mono);color:var(--acd);white-space:nowrap}\n.prog-bar{flex:1;height:6px;border-radius:6px;background:var(--line);overflow:hidden}\n.prog-bar i{display:block;height:100%;width:0;background:var(--ac);border-radius:6px;transition:width .35s ease}\n",
".acct.on{border-color:var(--acd);background:rgba(52,183,125,.06)}\n",
".tick{width:25px;height:25px;border-radius:7px;border:2px solid var(--line);background:#fff;cursor:pointer;\n  flex:none;display:grid;place-items:center;transition:all .16s;padding:0}\n.tick:hover{border-color:var(--acd)}\n.tick svg{opacity:0;transition:opacity .16s;width:14px;height:14px}\n.acct.on .tick{background:var(--ac);border-color:var(--ac)}\n.acct.on .tick svg{opacity:1}\n",
".acct.on .acct-n{color:var(--acd)}\n",
"  .acct.on{background:#fff}\n  .tick{border-color:#555}\n  .acct.on .tick{background:#fff;border-color:#555}\n  .acct.on .tick svg{opacity:1;stroke:#000}\n",
"  .prog{margin:14px 0 4px}.prog-bar{display:none}\n",
"  .tick{order:1}\n",
]:
    print(('ok  ' if frag in s else 'MISS'),'css:',frag[:34].replace('\n','/')); s=s.replace(frag,"",1)

# 4. the ticks paragraph in the closing note
o4="    <br><br><b>The ticks.</b> They keep your place while you work down the list, and that is all they do — they live in this browser on this device, so do not count on finding them again. Nothing here is worth coming back for: the value is in the three at the top, done now.\n"
print(('ok  ' if o4 in s else 'MISS'),'ticks note'); s=s.replace(o4,"",1)
io.open(p,'w',encoding='utf-8').write(s)
