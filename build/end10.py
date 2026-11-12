import io
p='courses/10-ai-tools.html'
s=io.open(p,encoding='utf-8').read()
a=s.index('end.innerHTML=`')
b=s.index('`;',s.index('<button class="nextbtn">',a))+2
new = """end.innerHTML=`<div class="ec"><h3>That\\u2019s the course.</h3>
  <p>What goes in, what comes back, and the features already running. Three things worth keeping:</p>
  <div class="ec-tk">
    <div class="ec-t"><span>\\u270b</span><div><b>The test is not \\u201Cis it secret\\u201D.</b> It is whether the text is yours to hand over \\u2014 a client\\u2019s email is theirs, and they were not asked.</div></div>
    <div class="ec-t"><span>\\u270d\\ufe0f</span><div><b>The output leaves with your name on it.</b> Fabricated citations look exactly like real ones, and \\u201Cthe AI said it\\u201D has been tried as a defence and lost.</div></div>
    <div class="ec-t"><span>\\ud83c\\udf99\\ufe0f</span><div><b>Some of it is already on.</b> Note-takers and inbox assistants arrived with an update, not with your consent \\u2014 check the participant list.</div></div>
  </div>
  <details class="ec-src"><summary>Sources and what is not sourced</summary>
  <ol>
<li>Samsung restricted staff use of generative AI after an engineer uploaded internal source code to ChatGPT, April\\u2013May 2023. Reported from Bloomberg: <a href="https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/" target="_blank" rel="noopener">Forbes Australia, 2 May 2023</a>.</li>
<li><i>Mata v. Avianca</i> (S.D.N.Y., June 2023) \\u2014 two lawyers sanctioned $5,000 after filing a brief citing cases ChatGPT had invented. Reported: <a href="https://www.abajournal.com/web/article/lawyers-who-doubled-down-and-defended-chatgpts-fake-cases-must-pay-5k-judge-says" target="_blank" rel="noopener">ABA Journal</a>.</li>
<li><i>Moffatt v. Air Canada</i>, British Columbia Civil Resolution Tribunal, 14 February 2024 \\u2014 Air Canada argued its chatbot was a separate entity responsible for its own answers; the tribunal rejected that and awarded about CAD $650. Analysis: <a href="https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/" target="_blank" rel="noopener">American Bar Association, Business Law Today</a>.</li>
<li>Prompt injection is LLM01 on the <a href="https://owasp.org/www-project-top-10-for-large-language-model-applications" target="_blank" rel="noopener">OWASP Top 10 for LLM Applications</a>, version 2025.</li>
  </ol>
  <div class="ec-src-note">Deliberately not stated here: which specific tool trains on your chats by default. Those defaults change \\u2014 Anthropic changed its consumer default in 2025 \\u2014 so any version printed in a course goes stale, which is why the action is to open the settings rather than learn an answer. Correct as described in November 2026. The note-taker and meeting examples describe how these features work; they are not drawn from a reported incident.</div></details>
  <div class="yourplan" id="yourplan"></div><button class="nextbtn">Finish Scene \\u2192</button></div>`;"""
s=s[:a]+new+s[b:]
io.open(p,'w',encoding='utf-8').write(s)
print('ok')
