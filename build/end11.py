import io
p='courses/11-data-classification.html'
s=io.open(p,encoding='utf-8').read()
a=s.index('end.innerHTML=`')
b=s.index('`;',s.index('<button class="nextbtn">',a))+2
new = """end.innerHTML=`<div class="ec"><h3>That\\u2019s the course.</h3>
  <p>One file, three exposures, and the label that settles it once. Three things worth keeping:</p>
  <div class="ec-tk">
    <div class="ec-t"><span>\\ud83d\\udccd</span><div><b>The risk is in the location, not the file.</b> Nothing about the spreadsheet changed between Monday and Friday. Who could reach it changed three times.</div></div>
    <div class="ec-t"><span>\\ud83d\\udd0d</span><div><b>A file holds more than the screen shows.</b> Deleted sheets, hidden rows, filtered data, document properties, the full image behind a crop. Rebuild rather than clean up.</div></div>
    <div class="ec-t"><span>\\u2696\\ufe0f</span><div><b>The level answers one question: how much harm if this got out.</b> Not who wrote it, not which folder it sits in, not what the footer says.</div></div>
  </div>
  <details class="ec-src"><summary>Sources and what is not sourced</summary>
  <ol>
<li>Police Service of Northern Ireland, August 2023 \\u2014 an FOI response published the surnames, initials, ranks and roles of 9,483 officers and staff; source data remained in a worksheet after the added sheets were deleted; file live from 14:31 to 17:27 on 8 August; \\u00a3750,000 fine announced 3 October 2024, reduced under the regulator\\u2019s public sector approach from a stated \\u00a35.6 million. <a href="https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/10/what-price-privacy-poor-psni-procedures-culminate-in-750k-fine/" target="_blank" rel="noopener">Information Commissioner\\u2019s Office</a>.</li>
<li>ISO/IEC 27001:2022 Annex A control 5.12 requires information to be classified but leaves the levels to the organisation \\u2014 \\u201Corganisations have the flexibility to establish and define their classification levels\\u201D. <a href="https://www.isms.online/iso-27001/annex-a/5-12-classification-of-information/" target="_blank" rel="noopener">Control 5.12 summary</a>; the standard itself is paywalled.</li>
<li>UK Government Security Classifications Policy uses three tiers \\u2014 OFFICIAL, SECRET, TOP SECRET \\u2014 with controls matched to \\u201Cpotential impact of a compromise, accidental loss or incorrect disclosure\\u201D. <a href="https://www.gov.uk/government/publications/government-security-classifications/government-security-classifications-policy-quick-read-html" target="_blank" rel="noopener">GOV.UK quick read</a>.</li>
<li>GDPR Article 9(1) special categories: racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data used to identify a person, health, and sex life or sexual orientation. <a href="https://gdpr-text.com/uk/read/article-9" target="_blank" rel="noopener">Article 9 text</a>.</li>
  </ol>
  <div class="ec-src-note">The four-level shape in the deep dive is a composite of common schemes, not a standard \\u2014 ISO leaves the levels to each organisation and UK government uses three, which is why the action is to find out what yours are called. The Q1 headcount file and its three stops are an illustration, not a reported case. Correct as described in November 2026; the \\u00a3750,000 figure is the fine as issued, and PSNI pursued an appeal, so check the current position if the outcome matters to your use.</div></details>
  <div class="yourplan" id="yourplan"></div><button class="nextbtn">Finish Scene \\u2192</button></div>`;"""
s=s[:a]+new+s[b:]
io.open(p,'w',encoding='utf-8').write(s)
print('ok')
