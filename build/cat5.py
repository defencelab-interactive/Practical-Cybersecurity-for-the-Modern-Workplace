import io
# ---------- index.html ----------
s=io.open('index.html',encoding='utf-8').read()
o="  ['byte','5a','Set Up MFA \\u2014 Step by Step','3 min','The settings path in each major account. The course says turn it on; this shows where.','']]],"
n="  ['byte','4b','Turn On MFA','~3 min','Your accounts in the order that matters, with what each company calls the setting.','bytes/04b-turn-on-mfa.html']]],"
assert o in s; s=s.replace(o,n,1)
s=s.replace("['course','4','Reused Passwords and the Second Lock','~7 min','How one reused password opens 47 accounts, and the habits that break the chain.'",
            "['course','4','Reused Passwords and the Second Lock','~7 min','How one reused password opens account after account, and the habits that break the chain.'",1)
io.open('index.html','w',encoding='utf-8').write(s); print('index ok')

# ---------- CATALOGUE.md ----------
c=io.open('CATALOGUE.md',encoding='utf-8').read()

# 1. drop Course 5 row
o="| 5 | **MFA: The Second Step** | MFA blocks 99% of automated attacks. Free, takes one minute, most people still haven't done it. | — | ~7 min |\n"
assert o in c; c=c.replace(o,"",1)

# 2. course 4 row -> real title + built
o="| 4 | **Passwords & Passphrases** | Complexity is a myth. Length wins. Here's how to build passwords that take centuries to crack. | 🔐 Describe your pattern → AI tests strength | ~7 min |"
n="| 4 | **Reused Passwords and the Second Lock** | One reused password, then account after account. Covers both passwords and MFA — the old Course 5 is folded in here. | 🔐 Describe your pattern → AI tests strength | ~7 min | **Built** |"
assert o in c; c=c.replace(o,n,1)

# 3. byte 5a -> 4b, built
o="| 5a | **Set Up MFA — Step by Step** | The settings path in each major account, with screenshots. The course says turn it on; this shows where. | 3 min | Course 4 | To build |"
n="| 4b | **Turn On MFA** | Your accounts in the order that matters, each with the company's own term for the setting, a link where one was confirmed, and a tick that saves. Add your own. | ~3 min | Course 4 | Built |"
assert o in c; c=c.replace(o,n,1)

# 4. totals
c=c.replace('**Total library:** 25 items (13 courses + 12 bytes), ~105 min combined. 15 built, 10 to build.',
            '**Total library:** 24 items (12 courses + 12 bytes), ~100 min combined. 16 built, 8 to build.',1)
c=c.replace('**Total: 13 courses, ~94 min**','**Total: 12 courses, ~87 min**',1)
c=c.replace('**Total Security Bytes: 12 items (5 built, 7 to build)**','**Total Security Bytes: 12 items (6 built, 6 to build)**',1)

# 5. retired table entry for Course 5
o="### Retired\n\n| Byte | Why it was dropped |\n|---|---|\n"
n=("### Retired\n\n**Course 5 — MFA: The Second Step.** Dropped. Course 4 already carries both halves: a reused\n"
   "password is the problem and the second factor is the answer, and splitting them made two thin courses\n"
   "out of one argument. The practical half moved to Byte 4b. Its old hook, “MFA blocks 99% of automated\n"
   "attacks”, was not reused — it is a vendor figure about a specific attack class and a specific period,\n"
   "and it gets quoted as if it were a general fact.\n\n"
   "| Byte | Why it was dropped |\n|---|---|\n")
assert o in c; c=c.replace(o,n,1)

# 6. learning path: fix the Auth block
o="| 7 | Course | Passwords & Passphrases | Auth | 7 min |\n| 8 | Byte | Create a Passphrase in 60 Seconds | Auth | 2 min |\n"
if o in c:
    n="| 7 | Course | Reused Passwords and the Second Lock | Auth | 7 min |\n| 8 | Byte | Build a Passphrase | Auth | 2 min |\n"
    c=c.replace(o,n,1); print('path auth ok')
o2="| 9 | Course | MFA: The Second Step | Auth | 7 min |\n| 10 | Byte | Set Up MFA — Step by Step | Auth | 3 min |\n"
if o2 in c:
    c=c.replace(o2,"| 9 | Byte | Turn On MFA | Auth | 3 min |\n",1); print('path mfa ok')
else:
    print('PATH MFA ROWS NOT MATCHED')
io.open('CATALOGUE.md','w',encoding='utf-8').write(c); print('catalogue ok')
