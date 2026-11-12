import io
p='courses/13-incident-response.html'
s=io.open(p,encoding='utf-8').read()

# wrap button + explanation in one card
old_r = """        <div class="or-pool">`;
      s.items.forEach((it,j)=>{
        h+=`<button class="or-i" data-ord="${i}-${j}"><span class="or-n"></span>
          <span class="or-t">${it.t}</span><span class="or-ok"></span></button>
          <div class="or-w"><div class="or-wi" id="orw-${i}-${j}">${it.why}</div></div>`;
      });"""
new_r = """        <div class="or-pool">`;
      s.items.forEach((it,j)=>{
        h+=`<div class="or-c" id="orc-${i}-${j}">
          <button class="or-i" data-ord="${i}-${j}"><span class="or-n"></span>
            <span class="or-t">${it.t}</span><span class="or-ok"></span></button>
          <div class="or-w"><div class="or-wi">${it.why}</div></div></div>`;
      });"""
print(('ok  ' if old_r in s else 'MISS'),'renderer'); s=s.replace(old_r,new_r,1)

# card styling moves to the wrapper; button becomes transparent
old_css = (".or-i{display:flex;align-items:center;gap:13px;background:var(--paper);border:1.5px solid var(--line);"
"border-radius:13px;padding:14px 16px;box-shadow:var(--sh);cursor:pointer;transition:all .16s;text-align:left;width:100%}\n"
".or-i:hover{border-color:var(--blue)}\n")
new_css = (".or-c{background:var(--paper);border:1.5px solid var(--line);border-radius:13px;overflow:hidden;"
"box-shadow:var(--sh);transition:border-color .16s}\n"
".or-c:hover{border-color:var(--blue)}\n"
".or-c.done:hover{border-color:var(--line)}\n"
".or-i{display:flex;align-items:center;gap:13px;background:none;border:0;"
"padding:14px 16px;cursor:pointer;text-align:left;width:100%}\n")
print(('ok  ' if old_css in s else 'MISS'),'card css'); s=s.replace(old_css,new_css,1)

for a,b in [
 (".or-i.picked .or-n{border-style:solid;border-color:var(--ac);background:var(--ac);color:#08301F}",
  ".or-i.picked .or-n{border-style:solid;border-color:var(--ac);background:var(--ac);color:#08301F}"),
 (".or-i.done+.or-w{max-height:300px}",".or-c.done .or-w{max-height:300px}"),
 (".or-wi{padding:11px 16px 4px 56px;font-size:14px;line-height:1.6;color:var(--ink-m)}",
  ".or-wi{padding:13px 17px 15px 56px;font-size:14px;line-height:1.6;color:var(--ink-m);border-top:1px solid var(--line)}"),
 ("@media (max-width:560px){.or-t{font-size:14.5px}.or-wi{padding-left:18px}}",
  "@media (max-width:560px){.or-t{font-size:14.5px}.or-wi{padding-left:17px}}"),
]:
    print(('ok  ' if a in s else 'MISS'),b[:46]); s=s.replace(a,b,1)

# grading must put done/right/wrong on the wrapper too
old_h = """        x.classList.add('done',ok?'right':'wrong');"""
new_h = """        x.classList.add('done',ok?'right':'wrong');
        const c=document.getElementById('orc-'+i+'-'+idx); if(c)c.classList.add('done',ok?'right':'wrong');"""
print(('ok  ' if old_h in s else 'MISS'),'grading'); s=s.replace(old_h,new_h,1)

old_rs = """      x.classList.remove('picked','done','right','wrong');
      delete x.dataset.pos; x.querySelector('.or-n').textContent='';
      x.querySelector('.or-ok').textContent='';});"""
new_rs = """      x.classList.remove('picked','done','right','wrong');
      delete x.dataset.pos; x.querySelector('.or-n').textContent='';
      x.querySelector('.or-ok').textContent='';
      const c=x.closest('.or-c'); if(c)c.classList.remove('done','right','wrong');});"""
print(('ok  ' if old_rs in s else 'MISS'),'reset'); s=s.replace(old_rs,new_rs,1)
io.open(p,'w',encoding='utf-8').write(s)
