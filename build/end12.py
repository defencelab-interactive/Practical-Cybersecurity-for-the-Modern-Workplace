import io
p='courses/12-file-sharing.html'
s=io.open(p,encoding='utf-8').read()
a=s.index('end.innerHTML=`')
b=s.index('`;',s.index('<button class="nextbtn">',a))+2
new = """end.innerHTML=`<div class="ec"><h3>That\\u2019s the course.</h3>
  <p>Three controls, one folder, and the thing nobody schedules. Three things worth keeping:</p>
  <div class="ec-tk">
    <div class="ec-t"><span>\\ud83d\\udd11</span><div><b>A link is a key, not a password.</b> It works for whoever ends up holding it, it is forwarded without anyone telling you, and it leaves you no list of who used it.</div></div>
    <div class="ec-t"><span>\\ud83d\\udcc1</span><div><b>The folder decides, not you.</b> Whatever the shared space is shared with, your file is now shared with \\u2014 and somebody else chose that, possibly years ago.</div></div>
    <div class="ec-t"><span>\\u23f3</span><div><b>Access outlasts its reason.</b> Projects end, people move, agencies change. Nothing removes the access, because nothing knows the reason is gone.</div></div>
  </div>
  <details class="ec-src"><summary>Sources and what is not sourced</summary>
  <ol>
<li>Microsoft AI research repository, 2020\\u20132023 \\u2014 an Azure Storage SAS link published for open-source models was \\u201Cconfigured to grant permissions on the entire storage account\\u201D with full control rather than read-only, exposing about 38TB including workstation backups, keys and over 30,000 internal Teams messages from 359 employees. Committed 20 July 2020 with expiry October 2021; expiry extended on 6 October 2021 to <b>6 October 2051</b>; reported by Wiz Research 22 June 2023, token invalidated 24 June 2023, disclosed 18 September 2023. <a href="https://www.wiz.io/blog/38-terabytes-of-private-data-accidentally-exposed-by-microsoft-ai-researchers" target="_blank" rel="noopener">Wiz Research</a>, the team that found it.</li>
  </ol>
  <div class="ec-src-note">One source, because one case carries the whole argument and the rest of this course is mechanism rather than claim. Deliberately not stated: which service defaults to \\u201Canyone with the link\\u201D, whether edit rights include re-sharing on <i>your</i> tools, and whether link-shared files can be found by search. Those differ by product, by plan and by what your organisation has configured, and they change \\u2014 which is why the course describes what the three controls decide and leaves you to read your own dialog. The contract scenario and the salary-file question are illustrations, not reported cases. Wiz is a security vendor writing about its own research; the dates and figures above are theirs, and Microsoft published its own account separately.</div></details>
  <div class="yourplan" id="yourplan"></div><button class="nextbtn">Finish Scene \\u2192</button></div>`;"""
s=s[:a]+new+s[b:]
io.open(p,'w',encoding='utf-8').write(s)
print('ok')
