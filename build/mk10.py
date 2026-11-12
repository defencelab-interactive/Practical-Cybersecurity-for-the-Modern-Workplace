import io,re
src=io.open('courses/08-phone-security.html',encoding='utf-8').read()
nodes=io.open('build/nodes10.js',encoding='utf-8').read().rstrip()

# ---- 1. title + rail header ----
src=src.replace('<title>Defence Lab · What Your Phone Can Reach</title>',
                '<title>Defence Lab · What You Paste Into AI</title>',1)
src=src.replace('<div class="eyebrow">Course 8 · Device Security</div>\n      <h1>What Your Phone Can Reach</h1>\n      <div class="r-sub">App permissions, public charging, and what to do in the first ten minutes after a phone goes missing.</div>',
 '<div class="eyebrow">Course 10 · AI Security</div>\n      <h1>What You Paste Into AI</h1>\n      <div class="r-sub">Where it goes, what comes back, and who is answerable for it.</div>',1)

# ---- 2. NODES ----
a=src.index('const NODES=[')
b=src.index('\n];',a)+3
src=src[:a]+nodes+src[b:]

# ---- 3. sort CSS (model on myth CSS block) ----
CSS=(".sort-spot{max-width:880px}\n"
".so{display:flex;flex-direction:column;gap:10px}\n"
".so-i{background:var(--paper);border:1.5px solid var(--line);border-radius:13px;overflow:hidden;box-shadow:var(--sh)}\n"
".so-t{padding:15px 18px 12px;font-size:15.5px;line-height:1.55;color:var(--ink)}\n"
".so-sub{display:block;margin-top:5px;font:500 13px var(--mono);color:var(--tm)}\n"
".so-btns{display:flex;gap:8px;padding:0 18px 15px}\n"
".so-b{flex:1;background:#fff;border:1.5px solid var(--line);border-radius:10px;padding:10px 8px;font:600 13px var(--body);color:var(--ink-m);cursor:pointer;transition:all .15s}\n"
".so-b:hover{border-color:var(--blue)}\n"
".so-i.done .so-btns{display:none}\n"
".so-v{display:none;align-items:center;gap:9px;padding:0 18px 13px}\n"
".so-i.done .so-v{display:flex}\n"
".so-tag{font:700 10px var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 9px;border-radius:20px}\n"
".so-i.right .so-tag{background:rgba(46,173,107,.14);color:var(--gr)}\n"
".so-i.wrong .so-tag{background:var(--rl);color:var(--rd)}\n"
".so-verdict{font:700 12.5px var(--body);color:var(--ink-m)}\n"
".so-w{max-height:0;overflow:hidden;transition:max-height .32s ease}\n"
".so-i.done .so-w{max-height:360px}\n"
".so-wi{padding:13px 18px 16px;font-size:14px;line-height:1.6;color:var(--ink-m);border-top:1px solid var(--line)}\n"
".so-bar{display:flex;align-items:center;gap:10px;margin-top:14px;font:600 12.5px var(--body);color:var(--tm)}\n"
".so-bar .so-prog{flex:1;height:4px;border-radius:4px;background:var(--line);overflow:hidden}\n"
".so-bar .so-prog i{display:block;height:100%;width:0;background:var(--ac);transition:width .3s ease}\n"
"@media (max-width:560px){.so-btns{flex-direction:column}}\n")
anc='.myth-spot{max-width:860px}'
i=src.index(anc); j=src.index('\n',i)+1
src=src[:j]+CSS+src[j:]

# ---- 4. sort renderer, before the myths branch ----
R=("""    } else if(s.type==='sort'){
      h+=`<div class="spot sort-spot"><div class="so">`;
      s.items.forEach((it,j)=>{
        h+=`<div class="so-i" id="so-${i}-${j}"><div class="so-t">${it.t}</div>
          <div class="so-btns">${s.buckets.map((bk,k)=>`<button class="so-b" data-sort="${i}-${j}-${k}">${bk}</button>`).join('')}</div>
          <div class="so-v"><span class="so-tag"></span><span class="so-verdict"></span></div>
          <div class="so-w"><div class="so-wi">${it.why}</div></div></div>`;
      });
      h+=`</div><div class="so-bar"><span id="sop-${i}">0 of ${s.items.length} sorted</span><span class="so-prog"><i id="sopb-${i}"></i></span></div>
        <div class="myth-fb" id="sofb-${i}"></div></div>`;
""")
anc2="    } else if(s.type==='myths'){"
src=src.replace(anc2, R+anc2, 1)

# ---- 5. sort click handler, before the myth handler ----
H=("""  // sort into two buckets
  const sb=e.target.closest('[data-sort]');
  if(sb){const[i,j,pick]=sb.dataset.sort.split('-').map(Number);const s=NODES[i].spot;const it=s.items[j];
    const el=document.getElementById('so-'+i+'-'+j);
    const ok=(pick===it.right);
    el.classList.add('done',ok?'right':'wrong');
    el.querySelector('.so-tag').textContent=s.buckets[it.right];
    el.querySelector('.so-verdict').textContent=ok?'You had it right.':'Other side.';
    if(ok)addXP(2);
    const all=[...document.querySelectorAll('[id^="so-'+i+'-"]')];
    const done=all.filter(x=>x.classList.contains('done')).length;
    const p=document.getElementById('sop-'+i);if(p)p.textContent=done+' of '+all.length+' sorted';
    const pb=document.getElementById('sopb-'+i);if(pb)pb.style.width=Math.round(done/all.length*100)+'%';
    if(done===all.length){
      const fb=document.getElementById('sofb-'+i);
      if(fb&&!fb.classList.contains('show')){fb.innerHTML=s.fb;fb.classList.add('show');
        recordAnswer(s.topic,all.filter(x=>x.classList.contains('right')).length>=4);markSeen(i);}
    }
    return;}
""")
anc3="  // myth-buster: judge a statement"
src=src.replace(anc3, H+anc3, 1)

io.open('courses/10-ai-tools.html','w',encoding='utf-8').write(src)
print('written, bytes:',len(src))
