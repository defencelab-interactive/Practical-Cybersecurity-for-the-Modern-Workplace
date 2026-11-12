import io
p='courses/11-data-classification.html'
s=io.open(p,encoding='utf-8').read()
reps=[
# clearer instruction in the node body
("It did not change at any point this week. Follow where it went, and watch who could reach it.",
 "It did not change at any point this week — not one cell. <b>Open all three stops below.</b> No stop is the answer on its own; what the exercise is showing you is the difference between them."),
# clearer prompt line
("q:'Tap each stop to see who could reach it there.',",
 "q:'Three stops, all of them yours to open. Each one shows who could reach the file at that point.',"),
# instruction styling + counter styling
(".trace-spot{max-width:880px}\n",
 ".trace-spot{max-width:880px}\n"
 ".tr-q{font:600 14px var(--body);color:var(--tm);margin-bottom:14px;line-height:1.55}\n"
 ".tr-bar2{display:flex;align-items:center;gap:10px;margin-top:4px;font:600 12.5px var(--body);color:var(--tm)}\n"
 ".tr-bar2 .tr-p{flex:1;height:4px;border-radius:4px;background:var(--line);overflow:hidden}\n"
 ".tr-bar2 .tr-p i{display:block;height:100%;width:0;background:var(--ac);transition:width .3s ease}\n"),
# counter markup
("""      h+=`</div><div class="myth-fb" id="trfb-${i}"></div></div>`;""",
 """      h+=`</div><div class="tr-bar2"><span id="trp-${i}">0 of ${s.stops.length} opened \\u2014 open them all to see the pattern</span>
        <span class="tr-p"><i id="trpb-${i}"></i></span></div>
        <div class="myth-fb" id="trfb-${i}"></div></div>`;"""),
# counter update in handler
("""    const all=[...document.querySelectorAll('[id^="tr-'+i+'-"]')];
    if(all.every(x=>x.classList.contains('done'))){""",
 """    const all=[...document.querySelectorAll('[id^="tr-'+i+'-"]')];
    const done=all.filter(x=>x.classList.contains('done')).length;
    const cp=document.getElementById('trp-'+i);
    if(cp)cp.textContent=done===all.length?('All '+all.length+' opened'):(done+' of '+all.length+' opened \\u2014 keep going, the pattern is in the difference');
    const cpb=document.getElementById('trpb-'+i);
    if(cpb)cpb.style.width=Math.round(done/all.length*100)+'%';
    if(all.every(x=>x.classList.contains('done'))){"""),
]
for a,b in reps:
    print(('ok  ' if a in s else 'MISS'),b[:60].replace('\n','/')); s=s.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(s)
