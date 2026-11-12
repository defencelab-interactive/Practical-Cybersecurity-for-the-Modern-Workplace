import io
p='courses/13-incident-response.html'
s=io.open(p,encoding='utf-8').read()
a=s.index('end.innerHTML=`')
b=s.index('`;',s.index('<button class="nextbtn">',a))+2
new = """end.innerHTML=`<div class="ec"><h3>That\\u2019s the course.</h3>
  <p>Four steps in order, and the thing that actually goes wrong. Three worth keeping:</p>
  <div class="ec-tk">
    <div class="ec-t"><span>\\ud83d\\udd0c</span><div><b>Disconnect first, and leave it running.</b> Unplugging stops the spread; shutting down throws away evidence held in memory that will not exist again.</div></div>
    <div class="ec-t"><span>\\u23f1\\ufe0f</span><div><b>Report before you are sure.</b> \\u201CI think I may have \\u2014 I am not certain\\u201D is a complete report. The hour spent checking first is the hour that costs money.</div></div>
    <div class="ec-t"><span>\\ud83d\\uddd1\\ufe0f</span><div><b>Do not tidy up.</b> Deleting the email, binning the file or rebuilding the machine removes what the responder needs and undoes nothing that already happened.</div></div>
  </div>
  <details class="ec-src"><summary>Sources and what is not sourced</summary>
  <ol>
<li>Isolation before anything else, and powering down only as a fallback: \\u201CDetermine which systems were impacted, and immediately isolate them\\u201D; \\u201CPower down devices if you are unable to disconnect them from the network\\u201D, which risks losing \\u201Cpotential evidence stored in volatile memory\\u201D; \\u201CBe sure to move through the first three steps in sequence.\\u201D <a href="https://www.cisa.gov/stopransomware/ive-been-hit-ransomware" target="_blank" rel="noopener">CISA, #StopRansomware</a>. Written for organisations and IT teams; this course translates the first step to what one person can do.</li>
<li>On silence after a click: \\u201Cthe stigma of clicking can prevent people reporting it, which then delays the incident response\\u201D, and \\u201CIt\\u2019s time for organisations to move away from using blame and fear around clicking links.\\u201D <a href="https://www.ncsc.gov.uk/sites/default/files/2026-08/Telling-users-to-%E2%80%98avoid-clicking-bad-links%E2%80%99-still-isn%E2%80%99t-working.pdf" target="_blank" rel="noopener">UK National Cyber Security Centre</a>.</li>
<li>GDPR Article 33(1): notification \\u201Cwithout undue delay and, where feasible, not later than 72 hours after having become aware of it\\u201D. <a href="https://gdpr-text.com/uk/read/article-33" target="_blank" rel="noopener">Article 33 text</a>.</li>
  </ol>
  <div class="ec-src-note">No figure is given for what delay costs, because the ones in circulation are vendor survey averages across wildly different incidents and they do not transfer to your situation. The argument here rests on the mechanism instead: what each step stops you losing. The renaming-files scenario is an illustration, not a reported case. The four-step order is this course\\u2019s own, built from the CISA sequence plus the NCSC point about reporting speed \\u2014 reporting comes second rather than last, which differs from some published mnemonics that put documenting before reporting. Outside the EU and UK, the notification deadline in that last source will be a different one.</div></details>
  <div class="yourplan" id="yourplan"></div><button class="nextbtn">Finish Scene \\u2192</button></div>`;"""
s=s[:a]+new+s[b:]
io.open(p,'w',encoding='utf-8').write(s); print('ok')
