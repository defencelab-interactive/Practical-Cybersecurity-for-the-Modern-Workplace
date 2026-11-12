import io,re
c=io.open('CATALOGUE.md',encoding='utf-8').read()

ROWS=[('Course','1','How a Breach Unfolds','General','6'),
('Byte','1b','Tools Worth Knowing About','General','4'),
('Course','2','How People Get Talked Into It','General','7'),
('Byte','2a','Your Verification Card','General','3'),
('Course','3','Screens, Paper and Devices','General','4'),
('Course','4','Reused Passwords and the Second Lock','Auth','7'),
('Byte','4a','Build a Passphrase','Auth','2'),
('Byte','4b','Turn On MFA','Auth','3'),
('Course','6','Spotting a Fake Email','Phishing','6'),
('Byte','6b','Link Inspector','Phishing','3'),
('Course','7','What Runs on Your Laptop','Devices','5'),
('Byte','7b','Your Home Network','Devices','2'),
('Byte','7f','Working Away From the Office','Devices','3'),
('Course','8','What Your Phone Can Reach','Devices','5'),
('Byte','8b','When Your Phone Goes Missing','Devices','2'),
('Course','9','What You Post About Work','Online','5'),
('Byte','9a',"Clean Up What's Public About You",'Online','3'),
('Course','10','What You Paste Into AI','AI','6'),
('Byte','10a','Anonymise an AI Prompt','AI','2'),
('Course','11','What Counts as Confidential','Data','5'),
('Byte','11b','Is This PII?','Data','2'),
('Course','12','File Sharing & Access','Data','6'),
('Course','13','The First 30 Minutes','Incident','6'),
('Byte','13a','STOP · DOCUMENT · REPORT','Incident','2')]

tbl='| Week | Type | # | Item | Group | Time |\n|---|---|---|---|---|---|\n'
for i,(ty,num,t,g,m) in enumerate(ROWS,1):
    tbl+=f'| {i} | {ty} | {num} | {t} | {g} | {m} min |\n'
total=sum(int(r[4]) for r in ROWS)

# replace the whole old path table
a=c.index('| Week | Type | Item | Group | Time |')
b=c.index('**Total: 26 items', a)
e=c.index('\n', c.index('\n', b)+1)
c=c[:a]+tbl+f'\n**Total: {len(ROWS)} items, ~{total} min.** One per week is 24 weeks; one per fortnight is about 11 months.\n'+c[e:]

# stale references elsewhere
fixes=[
("| Course | MFA: The Second Step | MFA for financial systems |\n| Byte | Set Up MFA — Step by Step | Action step |",
 "| Byte | Turn On MFA | Action step — MFA on the accounts that hold money first |"),
("| Course | MFA: The Second Step | MFA + passkeys — technical depth available |\n| Byte | Set Up MFA — Step by Step | Action step |",
 "| Byte | Turn On MFA | Action step — includes passkeys and hardware keys |"),
("| Byte | Set Up MFA — Step by Step | Day 1: enable MFA on all accounts |",
 "| Byte | Turn On MFA | Day 1: enable MFA, in the order the byte gives |"),
("| NIS2 Art. 21(2)(g) — Access control / credentials | Courses 4-5 (Passwords, MFA), Bytes 6-7 |",
 "| NIS2 Art. 21(2)(g) — Access control / credentials | Course 4 (passwords and MFA), Bytes 4a and 4b |"),
("| MFA: The Second Step | — | No AI block (procedural — enable MFA) |\n",""),
("| Course 4 | Passwords & Passphrases | `courses/04-passwords-mfa.html` | Built as *Reused Passwords and the Second Lock*, ~7 min — still **combined with Course 5** |",
 "| Course 4 | Reused Passwords and the Second Lock | `courses/04-passwords-mfa.html` | Built, ~7 min — carries both passwords and MFA; the old Course 5 is folded in |"),
]
for o,n in fixes:
    print(('ok  ' if o in c else 'MISS'), n[:58].replace('\n','/')); c=c.replace(o,n,1)
io.open('CATALOGUE.md','w',encoding='utf-8').write(c)
