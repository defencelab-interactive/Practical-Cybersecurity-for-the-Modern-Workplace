import io,re
# ---- 4b: drop dead CSS and the isOwn branch ----
p='bytes/04b-turn-on-mfa.html'
s=io.open(p,encoding='utf-8').read()
a=s.index('.own{display:flex;gap:9px;margin-top:11px}')
b=s.index('.acct-x{')
s=s[:a]+s[b:]
s=s.replace("  .own{flex-direction:column}\n","",1)
s=s.replace(".acct-x{flex:none;border:0;background:none;color:var(--mu);font:700 17px var(--body);cursor:pointer;padding:0 4px;line-height:1}\n.acct-x:hover{color:var(--rd)}\n","",1)
s=s.replace("""function rowHTML(a,isOwn){
  let line;
  if(isOwn) line='In its settings, look for <b>two-factor authentication</b> or <b>two-step verification</b>';
  else if(a.url) line='They call it <b>'+a.term+'</b>';
  else line='In their own help centre, search <b>'+a.term+'</b>';""",
"""function rowHTML(a){
  const line = a.url ? 'They call it <b>'+a.term+'</b>'
                     : 'In their own help centre, search <b>'+a.term+'</b>';""",1)
s=s.replace("""    ${isOwn?'<button class="acct-x" data-rm="'+a.id+'" aria-label="Remove">&times;</button>':go}\n""","""    ${go}\n""",1)
s=s.replace("${t.items.map(a=>rowHTML(a,false)).join('')}","${t.items.map(rowHTML).join('')}",1)
io.open(p,'w',encoding='utf-8').write(s)
print('4b cleaned | isOwn left:',len(re.findall(r'isOwn',s)),'| .own CSS left:',len(re.findall(r'\.own\{',s)))

# ---- 08b: honest claim + print ----
p2='bytes/08b-lost-phone.html'
t=io.open(p2,encoding='utf-8').read()
o="Ticks are saved in this browser so the list remembers where you got to."
n="Ticks keep your place while you work through it. They live in this browser only — print this or save it as a PDF, because the day you need the right-hand tab is the day you do not have the phone."
print(('ok  ' if o in t else 'MISS'),'08b claim'); t=t.replace(o,n,1)
io.open(p2,'w',encoding='utf-8').write(t)
