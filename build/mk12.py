import io
src=io.open('courses/11-data-classification.html',encoding='utf-8').read()
nodes=io.open('build/nodes12.js',encoding='utf-8').read().rstrip()

src=src.replace('<title>Defence Lab · What Counts as Confidential</title>',
                '<title>Defence Lab · Who Else Can Open This</title>',1)
src=src.replace('<div class="eyebrow">Course 11 · Data Protection</div>\n      <h1>What Counts as Confidential</h1>\n      <div class="r-sub">Why the same file changes risk depending on where it is, and how to tell the level without a committee.</div>',
 '<div class="eyebrow">Course 12 · Data Protection</div>\n      <h1>Who Else Can Open This</h1>\n      <div class="r-sub">What the sharing settings actually decide, and why access outlasts the reason for it.</div>',1)

a=src.index('const NODES=['); b=src.index('\n];',a)+3
src=src[:a]+nodes+src[b:]

CSS=(".share-spot{max-width:880px}\n"
".sh-file{display:inline-flex;align-items:center;gap:9px;background:var(--paper);border:1.5px solid var(--line);"
"border-radius:10px;padding:9px 14px;margin-bottom:16px;font:600 13px var(--mono);color:var(--ink);box-shadow:var(--sh)}\n"
".sh-dlg{background:var(--paper);border:1.5px solid var(--line);border-radius:15px;padding:6px 18px 18px;box-shadow:var(--sh)}\n"
".sh-row{padding:15px 0;border-bottom:1px solid var(--line)}\n"
".sh-row:last-of-type{border-bottom:0}\n"
".sh-lab{font:700 11px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--tm);margin-bottom:9px}\n"
".sh-opts{display:flex;gap:7px;flex-wrap:wrap}\n"
".sh-o{flex:1;min-width:150px;background:#fff;border:1.5px solid var(--line);border-radius:10px;padding:11px 13px;"
"font:600 13.5px var(--body);color:var(--ink-m);cursor:pointer;text-align:left;transition:all .15s}\n"
".sh-o:hover{border-color:var(--blue)}\n"
".sh-o.on{border-color:var(--ac);background:rgba(52,183,125,.09);color:var(--ink)}\n"
".sh-why{max-height:0;overflow:hidden;transition:max-height .3s ease}\n"
".sh-row.done .sh-why{max-height:260px}\n"
".sh-wi{display:flex;gap:11px;align-items:flex-start;margin-top:12px;font-size:14px;line-height:1.6;color:var(--ink-m)}\n"
".sh-dot{width:9px;height:9px;border-radius:50%;flex:none;margin-top:6px}\n"
".sh-r0 .sh-dot{background:var(--gr)}.sh-r1 .sh-dot{background:#D9A441}\n"
".sh-r2 .sh-dot{background:#D9A441}.sh-r3 .sh-dot{background:var(--rd)}\n"
".sh-row.done .sh-o:not(.on){opacity:.4}\n"
".sh-row.done .sh-o{cursor:default}\n"
".sh-go{width:100%;margin-top:16px;border:0;border-radius:11px;padding:13px;background:var(--ac);color:#08301F;"
"font:700 14.5px var(--body);cursor:pointer;transition:opacity .15s}\n"
".sh-go:disabled{opacity:.35;cursor:default}\n"
".sh-note{margin-top:12px;font:600 12.5px var(--body);color:var(--tm);text-align:center}\n"
"@media (max-width:560px){.sh-o{min-width:100%}}\n")
anc='.trace-spot{max-width:880px}'
i=src.index(anc); j=src.index('\n',i)+1
src=src[:j]+CSS+src[j:]

R=("""    } else if(s.type==='share'){
      h+=`<div class="spot share-spot"><div class="sh-file"><span>\\u{1F4C4}</span>${s.file}</div>
        <div class="sh-dlg">`;
      s.controls.forEach((c,ci)=>{
        h+=`<div class="sh-row" id="sh-${i}-${ci}"><div class="sh-lab">${c.label}</div>
          <div class="sh-opts">${c.opts.map((o,oi)=>`<button class="sh-o" data-sh="${i}-${ci}-${oi}">${o.t}</button>`).join('')}</div>
          <div class="sh-why"><div class="sh-wi" id="shw-${i}-${ci}"></div></div></div>`;
      });
      h+=`<button class="sh-go" id="shgo-${i}" data-shgo="${i}" disabled>Share it</button>
        <div class="sh-note" id="shn-${i}">Choose all three first</div></div>
        <div class="myth-fb" id="shfb-${i}"></div></div>`;
""")
src=src.replace("    } else if(s.type==='trace'){", R+"    } else if(s.type==='trace'){",1)

H=("""  // share dialog: pick each control, then share
  const so=e.target.closest('[data-sh]');
  if(so){const[i,ci,oi]=so.dataset.sh.split('-').map(Number);
    const row=document.getElementById('sh-'+i+'-'+ci);
    if(row.classList.contains('done'))return;
    row.querySelectorAll('.sh-o').forEach(x=>x.classList.remove('on'));
    so.classList.add('on'); row.dataset.pick=oi;
    const s=NODES[i].spot;
    const picked=s.controls.every((c,k)=>document.getElementById('sh-'+i+'-'+k).dataset.pick!==undefined);
    const go=document.getElementById('shgo-'+i);
    const nt=document.getElementById('shn-'+i);
    if(go)go.disabled=!picked;
    if(nt)nt.textContent=picked?'':'Choose all three first';
    return;}
  const sg=e.target.closest('[data-shgo]');
  if(sg){const i=+sg.dataset.shgo;const s=NODES[i].spot;
    let right=0;
    s.controls.forEach((c,ci)=>{
      const row=document.getElementById('sh-'+i+'-'+ci);
      const oi=+row.dataset.pick;const o=c.opts[oi];
      row.classList.add('done','sh-r'+o.risk);
      const w=document.getElementById('shw-'+i+'-'+ci);
      if(w)w.innerHTML='<span class="sh-dot"></span><span>'+o.why+'</span>';
      if(oi===c.best)right++;
    });
    sg.remove();
    const nt=document.getElementById('shn-'+i);
    if(nt)nt.textContent=right+' of '+s.controls.length+' as the task described';
    if(right===s.controls.length)addXP(6); else addXP(right*2);
    const fb=document.getElementById('shfb-'+i);
    if(fb&&!fb.classList.contains('show')){fb.innerHTML=s.fb;fb.classList.add('show');
      recordAnswer(s.topic,right>=2);markSeen(i);}
    return;}
""")
src=src.replace("  // trace: follow one file through its stops", H+"  // trace: follow one file through its stops",1)

io.open('courses/12-file-sharing.html','w',encoding='utf-8').write(src)
print('written',len(src))
