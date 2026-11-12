import io
p='courses/13-incident-response.html'
s=io.open(p,encoding='utf-8').read()

# ---------- renderer ----------
a=s.index("    } else if(s.type==='order'){")
b=s.index("    } else if(s.type==='share'){")
NEW_R = """    } else if(s.type==='order'){
      h+=`<div class="spot order-spot"><div class="or-sc"><span>\\u26A0\\uFE0F</span>${s.scenario}</div>
        <div class="or-how">Drag the rows by the grip, or use the arrows. Then check the order.</div>
        <div class="or-pool" id="orp-${i}">`;
      s.items.forEach((it,j)=>{
        h+=`<div class="or-c" data-oritem="${j}" data-node="${i}">
          <div class="or-i">
            <span class="or-n"></span>
            <span class="or-t">${it.t}</span>
            <span class="or-ok"></span>
            <span class="or-arrows">
              <button class="or-a" data-ormove="${i}--1" aria-label="Move up">\\u2191</button>
              <button class="or-a" data-ormove="${i}-1" aria-label="Move down">\\u2193</button>
            </span>
            <span class="or-grip" data-orgrip="${i}" aria-hidden="true">\\u2059</span>
          </div>
          <div class="or-w"><div class="or-wi">${it.why}</div></div></div>`;
      });
      h+=`</div><div class="or-bar">
        <button class="or-go" data-orcheck="${i}">Check the order</button>
        <span id="orn-${i}"></span>
        <button class="or-reset" data-ordreset="${i}" hidden>Try again</button></div>
        <div class="myth-fb" id="orfb-${i}"></div></div>`;
"""
s=s[:a]+NEW_R+s[b:]
print('renderer replaced')

# ---------- CSS ----------
ca=s.index(".order-spot{max-width:880px}")
cb=s.index("@media (max-width:560px){.or-t{font-size:14.5px}")
cb=s.index("\n",cb)+1
NEW_CSS = """.order-spot{max-width:880px}
.or-sc{display:flex;align-items:center;gap:10px;background:var(--rl);border:1.5px solid rgba(192,57,43,.3);border-radius:11px;padding:11px 15px;margin-bottom:11px;font:600 14px var(--body);color:var(--rd)}
.or-how{font-size:13.5px;line-height:1.55;color:var(--tm);margin-bottom:13px}
.or-pool{display:flex;flex-direction:column;gap:9px}
.or-c{background:var(--paper);border:1.5px solid var(--line);border-radius:13px;overflow:hidden;box-shadow:var(--sh);transition:border-color .16s,box-shadow .16s,opacity .16s}
.or-c.dragging{opacity:.55;border-color:var(--blue);box-shadow:0 10px 26px rgba(0,0,0,.22)}
.or-c.bump{animation:orbump .3s ease}
@keyframes orbump{0%{transform:scale(.985)}60%{transform:scale(1.012)}100%{transform:scale(1)}}
.or-i{display:flex;align-items:center;gap:12px;padding:13px 14px 13px 15px}
.or-n{width:27px;height:27px;border-radius:9px;flex:none;display:grid;place-items:center;font:700 13px var(--mono);background:var(--paper2,#E8EEEC);color:var(--ink-m);border:1.5px solid var(--line)}
.or-c.right .or-n{background:var(--gr);border-color:var(--gr);color:#fff}
.or-c.wrong .or-n{background:var(--rd);border-color:var(--rd);color:#fff}
.or-t{flex:1;min-width:0;font-size:15.5px;line-height:1.45;color:var(--ink)}
.or-ok{flex:none;font:700 10.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:4px 9px;border-radius:20px;display:none}
.or-c.right .or-ok{display:block;background:rgba(46,173,107,.15);color:var(--gr)}
.or-c.wrong .or-ok{display:block;background:var(--rl);color:var(--rd)}
.or-arrows{display:flex;flex-direction:column;gap:2px;flex:none}
.or-a{width:26px;height:19px;border:1.5px solid var(--line);background:#fff;border-radius:6px;color:var(--ink-m);font:700 11px var(--body);line-height:1;cursor:pointer;padding:0;display:grid;place-items:center}
.or-a:hover{border-color:var(--blue);color:var(--blue)}
.or-a:disabled{opacity:.3;cursor:default}
.or-grip{flex:none;width:26px;height:30px;display:grid;place-items:center;color:var(--ink-f);font-size:21px;cursor:grab;touch-action:none;user-select:none;border-radius:7px}
.or-grip:hover{background:rgba(78,124,168,.09);color:var(--blue)}
.or-grip:active{cursor:grabbing}
.or-pool.locked .or-grip,.or-pool.locked .or-arrows{display:none}
.or-w{max-height:0;overflow:hidden;transition:max-height .32s ease}
.or-c.done .or-w{max-height:300px}
.or-wi{padding:13px 17px 15px 54px;font-size:14px;line-height:1.6;color:var(--ink-m);border-top:1px solid var(--line)}
.or-bar{display:flex;align-items:center;gap:12px;margin-top:15px;font:600 12.5px var(--body);color:var(--tm);flex-wrap:wrap}
.or-go{border:0;border-radius:11px;padding:11px 20px;background:var(--ac);color:#08301F;font:700 14px var(--body);cursor:pointer}
.or-go:disabled{opacity:.4;cursor:default}
.or-reset{border:1.5px solid var(--line);background:var(--paper);color:var(--ink-m);border-radius:9px;padding:8px 14px;font:700 12px var(--body);cursor:pointer}
.or-reset:hover{border-color:var(--blue)}
@media (max-width:560px){.or-t{font-size:14.5px}.or-wi{padding-left:17px}.or-i{gap:9px;padding:12px}.or-grip{font-size:19px}}
"""
s=s[:ca]+NEW_CSS+s[cb:]
print('css replaced')

# ---------- handlers ----------
ha=s.index("  // order: tap the steps into sequence, then grade")
hb=s.index("  // share dialog: pick each control, then share")
NEW_H = """  // order: arrows move a row (drag is wired separately, below)
  const orm=e.target.closest('[data-ormove]');
  if(orm){const parts=orm.dataset.ormove.split('-');
    const i=+parts[0];const dir=parts.length>2?-1:+parts[1];
    const row=orm.closest('.or-c');const pool=row.parentElement;
    if(pool.classList.contains('locked'))return;
    const sib=dir<0?row.previousElementSibling:row.nextElementSibling;
    if(!sib)return;
    if(dir<0)pool.insertBefore(row,sib); else pool.insertBefore(sib,row);
    row.classList.remove('bump');void row.offsetWidth;row.classList.add('bump');
    orRenumber(i);
    return;}
  const orc=e.target.closest('[data-orcheck]');
  if(orc){const i=+orc.dataset.orcheck;const s2=NODES[i].spot;
    const pool=document.getElementById('orp-'+i);
    pool.classList.add('locked');
    let right=0;
    [...pool.children].forEach((row,pos)=>{
      const idx=+row.dataset.oritem;
      const ok=(s2.order[pos]===idx);
      row.classList.add('done',ok?'right':'wrong');
      row.querySelector('.or-ok').textContent=ok?'In place':'Out of order';
      if(ok)right++;
    });
    const nb=document.getElementById('orn-'+i);
    if(nb)nb.textContent=right+' of '+s2.items.length+' in the right place';
    orc.remove();
    const rs=document.querySelector('[data-ordreset="'+i+'"]');if(rs)rs.hidden=false;
    addXP(right*2);
    const fb=document.getElementById('orfb-'+i);
    if(fb&&!fb.classList.contains('show')){fb.innerHTML=s2.fb;fb.classList.add('show');
      recordAnswer(s2.topic,right>=3);markSeen(i);}
    return;}
  const orr=e.target.closest('[data-ordreset]');
  if(orr){const i=+orr.dataset.ordreset;
    const pool=document.getElementById('orp-'+i);
    pool.classList.remove('locked');
    [...pool.children].forEach(row=>{
      row.classList.remove('done','right','wrong');
      row.querySelector('.or-ok').textContent='';});
    const nb=document.getElementById('orn-'+i);if(nb)nb.textContent='';
    orr.hidden=true;
    const bar=orr.parentElement;
    if(!bar.querySelector('[data-orcheck]')){
      const btn=document.createElement('button');
      btn.className='or-go';btn.dataset.orcheck=i;btn.textContent='Check the order';
      bar.insertBefore(btn,bar.firstChild);}
    orRenumber(i);
    return;}
"""
s=s[:ha]+NEW_H+s[hb:]
print('handlers replaced')

# ---------- renumber + pointer drag, appended before </script> ----------
DRAG = """
/* order spot: live position numbers, arrow limits, and pointer drag that
   works with a mouse and with touch (the grip has touch-action:none so a
   drag does not scroll the page; everywhere else still scrolls normally) */
function orRenumber(i){
  const pool=document.getElementById('orp-'+i); if(!pool)return;
  const rows=[...pool.children];
  rows.forEach((row,k)=>{
    const n=row.querySelector('.or-n'); if(n)n.textContent=k+1;
    const ups=row.querySelector('[aria-label="Move up"]');
    const dns=row.querySelector('[aria-label="Move down"]');
    if(ups)ups.disabled=(k===0);
    if(dns)dns.disabled=(k===rows.length-1);
  });
}
(function orDrag(){
  let el=null,pool=null,node=null;
  function start(e){
    const grip=e.target.closest('[data-orgrip]'); if(!grip)return;
    const row=grip.closest('.or-c'); if(!row)return;
    pool=row.parentElement; if(pool.classList.contains('locked'))return;
    el=row; node=+grip.dataset.orgrip;
    el.classList.add('dragging');
    document.addEventListener('pointermove',move,{passive:false});
    document.addEventListener('pointerup',end);
    document.addEventListener('pointercancel',end);
    e.preventDefault();
  }
  function move(e){
    if(!el)return; e.preventDefault();
    const y=e.clientY;
    const sibs=[...pool.children].filter(x=>x!==el);
    let target=null;
    for(const sx of sibs){
      const r=sx.getBoundingClientRect();
      if(y<r.top+r.height/2){target=sx;break;}
    }
    if(target){ if(el.nextElementSibling!==target||el.parentElement!==pool) pool.insertBefore(el,target); }
    else if(pool.lastElementChild!==el) pool.appendChild(el);
    orRenumber(node);
  }
  function end(){
    if(!el)return;
    el.classList.remove('dragging');
    el.classList.remove('bump');void el.offsetWidth;el.classList.add('bump');
    el=null;pool=null;
    document.removeEventListener('pointermove',move);
    document.removeEventListener('pointerup',end);
    document.removeEventListener('pointercancel',end);
  }
  document.addEventListener('pointerdown',start);
})();
NODES.forEach((nd,i)=>{ if(nd.spot&&nd.spot.type==='order') setTimeout(()=>orRenumber(i),0); });
"""
k=s.rindex('</script>')
s=s[:k]+DRAG+'\n'+s[k:]
io.open(p,'w',encoding='utf-8').write(s)
print('drag appended')
