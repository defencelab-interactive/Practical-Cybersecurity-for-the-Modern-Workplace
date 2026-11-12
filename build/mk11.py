import io
src=io.open('courses/10-ai-tools.html',encoding='utf-8').read()
nodes=io.open('build/nodes11.js',encoding='utf-8').read().rstrip()

src=src.replace('<title>Defence Lab · What You Paste Into AI</title>',
                '<title>Defence Lab · What Counts as Confidential</title>',1)
src=src.replace('<div class="eyebrow">Course 10 · AI Security</div>\n      <h1>What You Paste Into AI</h1>\n      <div class="r-sub">Where it goes, what comes back, and who is answerable for it.</div>',
 '<div class="eyebrow">Course 11 · Data Protection</div>\n      <h1>What Counts as Confidential</h1>\n      <div class="r-sub">Why the same file changes risk depending on where it is, and how to tell the level without a committee.</div>',1)

a=src.index('const NODES=['); b=src.index('\n];',a)+3
src=src[:a]+nodes+src[b:]

CSS=(".trace-spot{max-width:880px}\n"
".tr-file{display:inline-flex;align-items:center;gap:9px;background:var(--paper);border:1.5px solid var(--line);"
"border-radius:10px;padding:9px 14px;margin-bottom:16px;font:600 13px var(--mono);color:var(--ink);box-shadow:var(--sh)}\n"
".tr-file span{font-size:15px}\n"
".tr{display:flex;flex-direction:column;gap:0}\n"
".tr-s{position:relative;padding-left:34px}\n"
".tr-s::before{content:'';position:absolute;left:10px;top:26px;bottom:-6px;width:2px;background:var(--line)}\n"
".tr-s:last-child::before{display:none}\n"
".tr-dot{position:absolute;left:4px;top:18px;width:14px;height:14px;border-radius:50%;background:var(--line);"
"border:2.5px solid var(--paper);transition:background .2s}\n"
".tr-s.done .tr-dot{background:var(--ac)}\n"
".tr-c{background:var(--paper);border:1.5px solid var(--line);border-radius:13px;overflow:hidden;"
"box-shadow:var(--sh);margin-bottom:12px}\n"
".tr-b{display:flex;align-items:center;gap:12px;width:100%;background:none;border:0;padding:15px 17px;"
"text-align:left;cursor:pointer;font:600 15px var(--body);color:var(--ink)}\n"
".tr-b:hover{background:rgba(78,124,168,.05)}\n"
".tr-s.done .tr-b{cursor:default}\n"
".tr-ic{font-size:19px;flex-shrink:0}\n"
".tr-t{flex:1;min-width:0}\n"
".tr-cue{font:600 11px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--blue);flex-shrink:0}\n"
".tr-s.done .tr-cue{display:none}\n"
".tr-w{max-height:0;overflow:hidden;transition:max-height .34s ease}\n"
".tr-s.done .tr-w{max-height:400px}\n"
".tr-wi{padding:0 17px 16px;border-top:1px solid var(--line);padding-top:13px}\n"
".tr-rl{display:flex;align-items:center;gap:10px;margin-bottom:9px}\n"
".tr-rn{font:700 12.5px var(--body);color:var(--ink)}\n"
".tr-bar{flex:1;height:5px;border-radius:5px;background:var(--line);overflow:hidden;min-width:60px}\n"
".tr-bar i{display:block;height:100%;width:0;border-radius:5px;transition:width .5s ease .1s}\n"
".tr-s.l1 .tr-bar i{background:var(--gr)}.tr-s.l2 .tr-bar i{background:#D9A441}.tr-s.l3 .tr-bar i{background:var(--rd)}\n"
".tr-who{font-size:14px;line-height:1.6;color:var(--ink-m)}\n"
"@media (max-width:560px){.tr-b{font-size:14.5px;gap:9px;padding:14px 14px}.tr-s{padding-left:28px}"
".tr-s::before{left:7px}.tr-dot{left:1px}}\n")
anc='.sort-spot{max-width:880px}'
i=src.index(anc); j=src.index('\n',i)+1
src=src[:j]+CSS+src[j:]

R=("""    } else if(s.type==='trace'){
      h+=`<div class="spot trace-spot"><div class="tr-file"><span>\\u{1F4C4}</span>${s.file}</div>
        <div class="tr-q">${s.q}</div><div class="tr">`;
      s.stops.forEach((st,j)=>{
        h+=`<div class="tr-s l${st.level}" id="tr-${i}-${j}"><div class="tr-dot"></div><div class="tr-c">
          <button class="tr-b" data-trace="${i}-${j}"><span class="tr-ic">${st.ic}</span>
            <span class="tr-t">${st.t}</span><span class="tr-cue">Who?</span></button>
          <div class="tr-w"><div class="tr-wi">
            <div class="tr-rl"><span class="tr-rn">${st.reach}</span><span class="tr-bar"><i></i></span></div>
            <div class="tr-who">${st.who}</div></div></div></div></div>`;
      });
      h+=`</div><div class="myth-fb" id="trfb-${i}"></div></div>`;
""")
src=src.replace("    } else if(s.type==='sort'){", R+"    } else if(s.type==='sort'){",1)

H=("""  // trace: follow one file through its stops
  const tb=e.target.closest('[data-trace]');
  if(tb){const[i,j]=tb.dataset.trace.split('-').map(Number);const s=NODES[i].spot;const st=s.stops[j];
    const el=document.getElementById('tr-'+i+'-'+j);
    if(el.classList.contains('done'))return;
    el.classList.add('done');
    const bar=el.querySelector('.tr-bar i');
    if(bar)setTimeout(()=>{bar.style.width=Math.round(st.level/s.stops.length*100)+'%';},60);
    addXP(2);
    const all=[...document.querySelectorAll('[id^="tr-'+i+'-"]')];
    if(all.every(x=>x.classList.contains('done'))){
      const fb=document.getElementById('trfb-'+i);
      if(fb&&!fb.classList.contains('show')){fb.innerHTML=s.fb;fb.classList.add('show');
        recordAnswer(s.topic,true);markSeen(i);}
    }
    return;}
""")
src=src.replace("  // sort into two buckets", H+"  // sort into two buckets",1)

io.open('courses/11-data-classification.html','w',encoding='utf-8').write(src)
print('written',len(src))
