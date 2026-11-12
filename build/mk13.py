import io
src=io.open('courses/12-file-sharing.html',encoding='utf-8').read()
nodes=io.open('build/nodes13.js',encoding='utf-8').read().rstrip()

src=src.replace('<title>Defence Lab · Share Links, Folders and Old Access</title>',
                '<title>Defence Lab · Disconnect, Report, Write It Down</title>',1)
src=src.replace('<div class="eyebrow">Course 12 · Data Protection</div>\n      <h1>Share Links, Folders and Old Access</h1>\n      <div class="r-sub">What the sharing settings actually decide, and why access outlasts the reason for it.</div>',
 '<div class="eyebrow">Course 13 · Incident Response</div>\n      <h1>Disconnect, Report, Write It Down</h1>\n      <div class="r-sub">The first few minutes after something goes wrong — and why the silence afterwards costs more than the mistake.</div>',1)

a=src.index('const NODES=['); b=src.index('\n];',a)+3
src=src[:a]+nodes+src[b:]

CSS=(".order-spot{max-width:880px}\n"
".or-sc{display:flex;align-items:center;gap:10px;background:var(--rl);border:1.5px solid rgba(192,57,43,.3);"
"border-radius:11px;padding:11px 15px;margin-bottom:15px;font:600 14px var(--body);color:var(--rd)}\n"
".or-pool{display:flex;flex-direction:column;gap:9px}\n"
".or-i{display:flex;align-items:center;gap:13px;background:var(--paper);border:1.5px solid var(--line);"
"border-radius:13px;padding:14px 16px;box-shadow:var(--sh);cursor:pointer;transition:all .16s;text-align:left;width:100%}\n"
".or-i:hover{border-color:var(--blue)}\n"
".or-i.picked{cursor:default}\n"
".or-n{width:27px;height:27px;border-radius:9px;border:1.5px dashed var(--line);flex:none;display:grid;"
"place-items:center;font:700 13px var(--mono);color:var(--ink-f);transition:all .18s}\n"
".or-i.picked .or-n{border-style:solid;border-color:var(--ac);background:var(--ac);color:#08301F}\n"
".or-i.right .or-n{background:var(--gr);border-color:var(--gr);color:#fff}\n"
".or-i.wrong .or-n{background:var(--rd);border-color:var(--rd);color:#fff}\n"
".or-t{flex:1;min-width:0;font-size:15.5px;line-height:1.45;color:var(--ink)}\n"
".or-ok{flex:none;font:700 10.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:4px 9px;border-radius:20px;display:none}\n"
".or-i.right .or-ok{display:block;background:rgba(46,173,107,.15);color:var(--gr)}\n"
".or-i.wrong .or-ok{display:block;background:var(--rl);color:var(--rd)}\n"
".or-w{max-height:0;overflow:hidden;transition:max-height .32s ease}\n"
".or-i.done+.or-w{max-height:300px}\n"
".or-wi{padding:11px 16px 4px 56px;font-size:14px;line-height:1.6;color:var(--ink-m)}\n"
".or-bar{display:flex;align-items:center;gap:11px;margin-top:15px;font:600 12.5px var(--body);color:var(--tm)}\n"
".or-reset{border:1.5px solid var(--line);background:var(--paper);color:var(--ink-m);border-radius:9px;"
"padding:7px 13px;font:700 12px var(--body);cursor:pointer}\n"
".or-reset:hover{border-color:var(--blue)}\n"
"@media (max-width:560px){.or-t{font-size:14.5px}.or-wi{padding-left:18px}}\n")
anc='.share-spot{max-width:880px}'
i=src.index(anc); j=src.index('\n',i)+1
src=src[:j]+CSS+src[j:]

R=("""    } else if(s.type==='order'){
      h+=`<div class="spot order-spot"><div class="or-sc"><span>\\u26A0\\uFE0F</span>${s.scenario}</div>
        <div class="or-pool">`;
      s.items.forEach((it,j)=>{
        h+=`<button class="or-i" data-ord="${i}-${j}"><span class="or-n"></span>
          <span class="or-t">${it.t}</span><span class="or-ok"></span></button>
          <div class="or-w"><div class="or-wi" id="orw-${i}-${j}">${it.why}</div></div>`;
      });
      h+=`</div><div class="or-bar"><span id="orn-${i}">Tap them in order \\u2014 first action first</span>
        <button class="or-reset" id="orr-${i}" data-ordreset="${i}" hidden>Start over</button></div>
        <div class="myth-fb" id="orfb-${i}"></div></div>`;
""")
src=src.replace("    } else if(s.type==='share'){", R+"    } else if(s.type==='share'){",1)

H=("""  // order: tap the steps into sequence, then grade
  const or=e.target.closest('[data-ord]');
  if(or){const[i,j]=or.dataset.ord.split('-').map(Number);const s=NODES[i].spot;
    if(or.classList.contains('picked'))return;
    const pool=[...document.querySelectorAll('[id$="-pool"],[data-ord^="'+i+'-"]')].filter(x=>x.dataset&&x.dataset.ord);
    const taken=pool.filter(x=>x.classList.contains('picked')).length;
    or.classList.add('picked'); or.dataset.pos=taken;
    or.querySelector('.or-n').textContent=taken+1;
    const nb=document.getElementById('orn-'+i);
    if(nb)nb.textContent=(taken+1)+' of '+s.items.length+' placed';
    if(taken+1===s.items.length){
      let right=0;
      pool.forEach(x=>{
        const idx=+x.dataset.ord.split('-')[1];const pos=+x.dataset.pos;
        const ok=(s.order[pos]===idx);
        x.classList.add('done',ok?'right':'wrong');
        x.querySelector('.or-ok').textContent=ok?'In place':'Out of order';
        if(ok)right++;
      });
      if(nb)nb.textContent=right+' of '+s.items.length+' in the right place';
      const rs=document.getElementById('orr-'+i); if(rs)rs.hidden=false;
      addXP(right*2);
      const fb=document.getElementById('orfb-'+i);
      if(fb&&!fb.classList.contains('show')){fb.innerHTML=s.fb;fb.classList.add('show');
        recordAnswer(s.topic,right>=3);markSeen(i);}
    }
    return;}
  const orr=e.target.closest('[data-ordreset]');
  if(orr){const i=+orr.dataset.ordreset;
    document.querySelectorAll('[data-ord^="'+i+'-"]').forEach(x=>{
      x.classList.remove('picked','done','right','wrong');
      delete x.dataset.pos; x.querySelector('.or-n').textContent='';
      x.querySelector('.or-ok').textContent='';});
    const nb=document.getElementById('orn-'+i);
    if(nb)nb.textContent='Tap them in order \\u2014 first action first';
    orr.hidden=true;
    return;}
""")
src=src.replace("  // share dialog: pick each control, then share", H+"  // share dialog: pick each control, then share",1)

io.open('courses/13-incident-response.html','w',encoding='utf-8').write(src)
print('written',len(src))
