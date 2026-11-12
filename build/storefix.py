import io

SHIM = """/* storage: the Defence Lab host provides window.storage; standalone falls back
   to localStorage. Both can fail (private window, blocked site data), so every
   call is wrapped and the page works with none of it. */
const DL={
  async get(k){try{
    if(window.storage){const r=await window.storage.get(k);return r&&r.value?r.value:null;}
    return localStorage.getItem(k);
  }catch(e){return null}},
  async set(k,v){try{
    if(window.storage)return await window.storage.set(k,v);
    localStorage.setItem(k,v);
  }catch(e){}},
  async del(k){try{
    if(window.storage)return await window.storage.delete(k);
    localStorage.removeItem(k);
  }catch(e){}}
};
"""

def patch(path, reps, anchor):
    s=io.open(path,encoding='utf-8').read()
    for a,b in reps:
        if a not in s: print('  MISS',path,'|',a[:60]); continue
        s=s.replace(a,b,1)
    i=s.index(anchor)
    s=s[:i]+SHIM+s[i:]
    io.open(path,'w',encoding='utf-8').write(s); print('  ok',path)

print('04b'); patch('bytes/04b-turn-on-mfa.html',[
("""async function save(){
  try{
    if(!window.storage)return;
    await window.storage.set('turn-on-mfa',JSON.stringify({ticked,own}));
  }catch(e){}
}
async function load(){
  try{
    if(window.storage){
      const r=await window.storage.get('turn-on-mfa');
      if(r&&r.value){const d=JSON.parse(r.value); ticked=d.ticked||{}; own=d.own||[];}
    }
  }catch(e){}
  render();
}""",
"""async function save(){ await DL.set('turn-on-mfa',JSON.stringify({ticked,own})); }
async function load(){
  try{
    const v=await DL.get('turn-on-mfa');
    if(v){const d=JSON.parse(v); ticked=d.ticked||{}; own=d.own||[];}
  }catch(e){}
  render();
}"""),
],"/* persistence — survives closing the tab */")

print('07b'); patch('bytes/07b-home-wifi.html',[
("""async function save(){try{if(!window.storage)return;
  await window.storage.set('home-wifi',JSON.stringify([...document.querySelectorAll('.step')].map(x=>x.classList.contains('on')?1:0)));}catch(e){}}""",
 """async function save(){await DL.set('home-wifi',JSON.stringify([...document.querySelectorAll('.step')].map(x=>x.classList.contains('on')?1:0)));}"""),
("""async function load(){try{if(!window.storage)return;const r=await window.storage.get('home-wifi');if(!r||!r.value)return;""",
 """async function load(){try{const v=await DL.get('home-wifi');if(!v)return;const r={value:v};"""),
],"async function save(){await DL.set('home-wifi'")

print('08b'); patch('bytes/08b-lost-phone.html',[
("""    if(!window.storage)return;
    const prep=""","""    const prep="""),
("""    await window.storage.set('lost-phone',JSON.stringify({prep,done}));""",
 """    await DL.set('lost-phone',JSON.stringify({prep,done}));"""),
("""    if(!window.storage)return;
    const r=await window.storage.get('lost-phone'); if(!r||!r.value)return;
    const d=JSON.parse(r.value);""",
 """    const v=await DL.get('lost-phone'); if(!v)return;
    const d=JSON.parse(v);"""),
],"/* persistence — survives closing the tab */")

print('02a'); patch('bytes/02a-verification-card.html',[
(""" try{window.storage&&window.storage.delete('verification-card');}catch(e){}""",
 """ DL.del('verification-card');"""),
(""" try{ if(window.storage) await window.storage.set('verification-card',JSON.stringify({ctx,vals})); }catch(e){}""",
 """ await DL.set('verification-card',JSON.stringify({ctx,vals}));"""),
("""  if(!window.storage)return;
  const r=await window.storage.get('verification-card');""",
 """  const v=await DL.get('verification-card'); if(!v)return;
  const r={value:v};"""),
],"async function save")
