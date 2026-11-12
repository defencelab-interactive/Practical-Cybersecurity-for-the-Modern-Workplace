# Defence Lab — Course Catalogue & Learning Paths

## Overview

Cybersecurity awareness training for non-technical employees. Two content formats:

- **Courses** — 10-12 slides, 6-8 min. Story-driven, interactive, practice-oriented.
- **Security Bytes** — 4-5 slides, 2-3 min. One specific action, step-by-step, no theory.

Courses build understanding. Bytes build habits. Both work independently. Both stack into learning paths.

**Total library:** 24 items (12 courses + 12 bytes), ~100 min combined. 16 built, 8 to build.

---

## Courses

Each course follows a consistent structure: story → content with interactive elements → quiz → action → summary with personal action plan.

### 🟢 General Awareness

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 1 | **Security Basics: Why One Setting Matters** | One missing setting cost a company $2.4B. What are the basics that actually prevent this? | — | ~7 min |
| 2 | **Social Engineering: How People Get Played** | Attackers don't hack systems — they hack people. Pretexting, tailgating, baiting, and how to see it coming. | 🎭 Role-play: AI plays social engineer | ~7 min |
| 3 | **Physical Security: Desks, Screens, Printers** | A photographer, an unlocked screen, and a $50K fine. Physical security for the modern office. | 📸 Upload desk photo → AI spots risks | ~6 min |

### 🔑 Authentication

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 4 | **Reused Passwords and the Second Lock** | One reused password, then account after account. Covers both passwords and MFA — the old Course 5 is folded in here. | 🔐 Describe your pattern → AI tests strength | ~7 min | **Built** |

### 🎣 Phishing & Social Engineering

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 6 | **Phishing: Spot, Check, Report** | Phishing is the #1 attack vector — involved in 90%+ of breaches. Learn to spot it, check it, report it. | 📨 Paste email → AI analyzes + 🎭 BEC role-play | ~8 min |

### 💻 Device Security

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 7 | **Laptop Security Settings** | An unlocked laptop left for 90 seconds led to a $2.3M ransomware attack. Three settings prevent this. | — | ~6 min |
| 8 | **Phone Security Settings** | Your phone holds more access than your laptop — email, bank, authenticator, contacts. Is it secured? | — | ~6 min |

### 🌐 Online Presence

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 9 | **Social Media: What You're Really Sharing** | One LinkedIn photo gave an attacker everything they needed for a $340K fraud. | 📨 Paste post + 📸 Upload photo → AI shows attacker view | ~8 min |

### 🤖 AI Security

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 10 | **What You Paste Into AI** | Six things people paste, and where the line actually is. Then what comes back, and who answers for it. | 📨 Paste prompt → billboard test + anonymized version | ~6 min | **Built** |

### 📂 Data Protection

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 11 | **What Counts as Confidential** | One file, three places it went this week, three different exposures. Then the PSNI spreadsheet. | 🏋️ Describe a file → AI classifies with reasoning | ~5 min | **Built** |
| 12 | **File Sharing & Access** | "Anyone with the link" is almost never the right setting for confidential data. | 📨 Describe sharing setup → AI checks | ~6 min |

### 🚨 Incident Response

| # | Course | Hook | AI Buddy | Time |
|---|---|---|---|---|
| 13 | **Incident Response: First 30 Minutes** | The difference between a $0 incident and a $280K loss is 30 seconds of action. STOP · DOCUMENT · REPORT. | 🏋️ Describe incident → AI coaches through STOP/DOC/REPORT | ~7 min |

**Total: 12 courses, ~87 min**

### Opening mechanics used so far

No two courses open the same way. Spot types built to date:

| Course | Opening | Mechanic |
|---|---|---|
| 1 | Story — how a breach unfolds | narrative + `predict` |
| 2 | The attacker's side of the call | narrative + `predict` |
| 3 | Audit your own desk right now | `audit` |
| 4 | One forum password, then the cascade | narrative + `quiz` |
| 6 | Two emails, one is fake | `compare` |
| 7 | Three things people believe | `myths` |
| 8 | Which would hurt more to lose | `weigh` |
| 9 | Guess how much the post gives away | `estimate` |
| 10 | Sort six things into fine / not mine | `sort` |
| 11 | Follow one file through three places | `trace` |

Other spot types available mid-course: `quiz`, `predict`, `experience`, `checklist`, `takeaways`, `slider`, `flags`, `scan`.

### Accuracy rule

Every factual claim is sourced before it is written, not after. A claim that cannot be shown with a quote is either cut or labelled as a composed scenario in the text itself. Each course carries a **Sources and what is not sourced** block in its end card. The register of what was checked, what needs human confirmation and what is uncertain lives in `FACT-CHECK.md`.

### Course structure (per course)

| Element | Quantity | Purpose |
|---|---|---|
| Story slide | 1 | Emotional anchor — real incident, real consequences |
| Early win | 1 | Quick action or recognition in the first 2-3 slides — immediate sense of progress |
| Content slides | 4-6 | Core concepts with expandable accordions for depth |
| Quizzes | 1-2 | Formative — wager mechanic (Sure ×3 / Pretty sure ×2 / Guessing ×1) with remediation links |
| Interactive | 0-2 | Spot the Threat, Drag to Classify, Timeline, Spot the Risk, Spot the Leak, Phishing or Legit |
| Reflection | 1 | Generation-effect prompt (count, name, time yourself — not yes/no) |
| Breather | 1 | Animated scene — cognitive reset, visual metaphor |
| Action | 1-2 | Concrete task: "do this now" or "add to my action plan" (saved tasks shown on summary card) |
| Summary | 1 | Key takeaways + personal action plan auto-filled from saved tasks + link to paired Security Byte |

### Interactive mechanics across the library

| Mechanic | Courses | Skill |
|---|---|---|
| Spot the Threat | Course 4 (phishing email) | Identify red flags in a suspicious email |
| Spot the Risk | Course 7 (LinkedIn post) | Identify information leakage in social media |
| Spot the Leak | Course 8 (AI prompts) | Classify prompts as safe or data-leaking |
| Phishing or Legit? | Course 4 (messages) | Sort real vs. fake messages |
| Drag to Classify | Course 9 (data items) | Apply 4-level classification framework |
| Timeline | Courses 1, 7 | Walk through an attack step by step |
| Wager Quiz | All courses | Metacognitive calibration + retrieval practice |

### Optional advanced content

Six courses include a **"Want to know more?"** expandable section for technically curious learners. These are clearly marked as optional and don't affect course completion.

| Course | Advanced topic |
|---|---|
| 2 | How password cracking works (hash tables, rainbow tables) |
| 3 | How passkeys work under the hood (WebAuthn/FIDO2) |
| 4 | How email spoofing works (SPF/DKIM/DMARC) |
| 5 | How full-disk encryption works (AES-256) |
| 8 | How LLMs handle your data (token prediction, enterprise vs. public) |
| 9 | Zero trust architecture basics |

---

## Security Bytes

A Byte earns its place if it is a **tool or an artefact people come back to**. A one-off
instruction, or a retelling of its own course, does not — that was the lesson of the retired
breach-check Byte, and the list below was rebuilt on it.

**A Byte may not depend on the reader coming back to it.** People open a module once, often
through an LMS, in whatever browser is to hand, and then leave. Anything whose value only pays
off on a return visit — a list you build up, a profile you fill in over time — is worth nothing to
them. In-session state (ticks that keep your place while you work down a list) is fine; promises
that the page will remember are not. Whatever is worth keeping leaves as **print or PDF**.
Byte 4b lost its “add your own accounts” field to this rule.

**Storage:** `window.storage` exists only inside the Defence Lab host. Standalone pages must fall
back to `localStorage`, wrapped, and work with neither. Every Byte that stores anything gets a
reload test before it ships.

**Numbering:** a Byte carries the number of the course it pairs with, plus a letter — Byte 6b
belongs with Course 6. Files follow the same scheme (`bytes/06b-link-inspector.html`).

| # | Byte | What it is | Time | Pairs with | Status |
|---|---|---|---|---|---|
| 1b | **Tools Worth Knowing About** | Filterable rundown of security tools by OS, browser and phone | ~4 min | Course 1 | Built |
| 2a | **Your Verification Card** | Three questions about where you work, then a card naming who confirms what. Saves and prints. | ~3 min | Course 2 | Built |
| 4a | **Build a Passphrase** | Generator: four words, separators, strength shown as you go | 2 min | Course 4 | To build |
| 4b | **Turn On MFA** | Your accounts in the order that matters, each with the company's own term for the setting, a link where one was confirmed, and a tick that saves. Add your own. | ~3 min | Course 4 | Built |
| 6b | **Link Inspector** | Paste a URL and see where it really goes — domain, @ trick, punycode, lookalikes. Runs in the browser. | ~3 min | Course 6 | Built |
| 7b | **Your Home Network** | Paste your WiFi name and see what it gives away (surname, address, router model, ISP default), then three router settings | 2 min | Course 7 | Built |
| 7f | **Working Away From the Office** | Laptop settings, cafés and travel in one reference *(merges the old 7a, 7c, 7e)* | 3 min | Courses 7–8 | To build |
| 8b | **When Your Phone Goes Missing** | Two tabs: the three settings that only work beforehand, and the lock→notify→passwords→wipe order for when it is gone | ~2 min | Course 8 | Built |
| 9a | **Clean Up What's Public About You** | LinkedIn settings, old accounts, searching for yourself *(merges the old 9a, 9b)* | 3 min | Course 9 | To build |
| 10a | **Anonymise an AI Prompt** | Paste a prompt; names, companies and project details are highlighted with suggested replacements | 2 min | Course 10 | To build |
| 11b | **Is This PII?** | Eight examples to sort, including the edge cases that catch people | 2 min | Course 11 | To build |
| 13a | **STOP · DOCUMENT · REPORT** | A card you fill in once, save and print | 2 min | Course 13 | To build |

**Total Security Bytes: 12 items (6 built, 6 to build)**

### Retired

**Course 5 — MFA: The Second Step.** Dropped. Course 4 already carries both halves: a reused
password is the problem and the second factor is the answer, and splitting them made two thin courses
out of one argument. The practical half moved to Byte 4b. Its old hook, “MFA blocks 99% of automated
attacks”, was not reused — it is a vendor figure about a specific attack class and a specific period,
and it gets quoted as if it were a general fact.

| Byte | Why it was dropped |
|---|---|
| Check If You've Been Breached | A single instruction to visit one external site. Nothing to return to. |
| Spot a Social Engineering Attempt | Five tactics and three examples — which is what Course 2 does, in more depth. |
| Safe Browsing: Three Rules | What was still live in it is done better by the Link Inspector. |
| Your Company's Security Policy | A template that says "ask your own company". Nothing of ours in it. |
| The Clean Desk Checklist | Course 3 closes it in its own checklist. |
| Secure Printing | Same — Course 3 covers it where it is relevant. |
| The 5-Second Email Check | That is Course 6, entire. |
| How to Report a Phishing Email | One paragraph, already a checklist item in Course 6. |
| USB Drives: Don't Plug and Pray | Course 2 covers baiting, including the keyboard-emulation detail in a deep dive. |
| App Permission Cleanup | A one-off instruction with nothing to come back for. |
| Spot a Deepfake Call | Moved into a deep dive in Course 6. |
| Classify This: Quick Exercise | Course 11 will carry the sorting exercise itself. |


## Learning Paths

### Full Path: Practical Cybersecurity

The complete curriculum. Recommended deployment: one item per 1-2 weeks over 6 months, or one item per month over 12 months.

**Sequence:**

| Week | Type | # | Item | Group | Time |
|---|---|---|---|---|---|
| 1 | Course | 1 | How a Breach Unfolds | General | 6 min |
| 2 | Byte | 1b | Tools Worth Knowing About | General | 4 min |
| 3 | Course | 2 | How People Get Talked Into It | General | 7 min |
| 4 | Byte | 2a | Your Verification Card | General | 3 min |
| 5 | Course | 3 | Screens, Paper and Devices | General | 4 min |
| 6 | Course | 4 | Reused Passwords and the Second Lock | Auth | 7 min |
| 7 | Byte | 4a | Build a Passphrase | Auth | 2 min |
| 8 | Byte | 4b | Turn On MFA | Auth | 3 min |
| 9 | Course | 6 | Spotting a Fake Email | Phishing | 6 min |
| 10 | Byte | 6b | Link Inspector | Phishing | 3 min |
| 11 | Course | 7 | What Runs on Your Laptop | Devices | 5 min |
| 12 | Byte | 7b | Your Home Network | Devices | 2 min |
| 13 | Byte | 7f | Working Away From the Office | Devices | 3 min |
| 14 | Course | 8 | What Your Phone Can Reach | Devices | 5 min |
| 15 | Byte | 8b | When Your Phone Goes Missing | Devices | 2 min |
| 16 | Course | 9 | What You Post About Work | Online | 5 min |
| 17 | Byte | 9a | Clean Up What's Public About You | Online | 3 min |
| 18 | Course | 10 | What You Paste Into AI | AI | 6 min |
| 19 | Byte | 10a | Anonymise an AI Prompt | AI | 2 min |
| 20 | Course | 11 | What Counts as Confidential | Data | 5 min |
| 21 | Byte | 11b | Is This PII? | Data | 2 min |
| 22 | Course | 12 | File Sharing & Access | Data | 6 min |
| 23 | Course | 13 | The First 30 Minutes | Incident | 6 min |
| 24 | Byte | 13a | STOP · DOCUMENT · REPORT | Incident | 2 min |

**Total: 24 items, ~99 min.** One per week is 24 weeks; one per fortnight is about 11 months.

Pattern: Course → paired Byte → next Course → paired Byte. The course builds understanding, the Byte locks in the action. General Awareness comes first — it sets the foundation for everything else.

---

### Role-Based Paths

Each path selects the most relevant courses and bytes for a specific role. Items are ordered by priority.

#### Finance & Accounting
| Type | Item | Why |
|---|---|---|
| Course | Security Basics: Why One Setting Matters | Foundation — sets the stakes |
| Course | Social Engineering: How People Get Played | Social engineering — finance is the #1 target for pretexting |
| Course | Phishing: Spot, Check, Report | Phishing + BEC — #1 risk for finance |
| Byte | The 5-Second Email Check | Daily habit for email-heavy role |
| Byte | Turn On MFA | Action step — MFA on the accounts that hold money first |
| Course | Incident Response: First 30 Minutes | Incident response — wire fraud recovery |
| Byte | STOP · DOCUMENT · REPORT Card | Emergency reference |
| **Total** | **5 courses + 3 bytes** | **~40 min** |

#### Marketing & Communications
| Type | Item | Why |
|---|---|---|
| Course | Social Media: What You're Really Sharing | Social media = attack surface for marketing |
| Byte | LinkedIn Privacy in 2 Minutes | Action step |
| Course | AI Tools: Safe Use at Work | AI tools used daily for content |
| Byte | How to Anonymize an AI Prompt | Practical skill |
| Course | Phishing: Spot, Check, Report | Phishing — universal risk |
| Byte | The 5-Second Email Check | Daily habit |
| Course | Data Classification: Four Levels | Customer data handling |
| **Total** | **4 courses + 3 bytes** | **~33 min** |

#### Engineering & IT
| Type | Item | Why |
|---|---|---|
| Course | Passwords & Passphrases | Credential hygiene |
| Byte | Turn On MFA | Action step — includes passkeys and hardware keys |
| Course | AI Tools: Safe Use at Work | Shadow AI, code in prompts |
| Byte | How to Anonymize an AI Prompt | Daily skill for developers |
| Course | Laptop Security Settings | Device security |
| Course | Incident Response: First 30 Minutes | Incident reporting for technical staff |
| **Total** | **5 courses + 2 bytes** | **~37 min** |

#### Executives & Leadership
| Type | Item | Why |
|---|---|---|
| Course | Security Basics: Why One Setting Matters | Business impact framing |
| Course | AI Tools: Safe Use at Work | Deepfakes target executives |
| Byte | Spot a Deepfake Call | Specific defense for exec-targeted attacks |
| Course | Social Media: What You're Really Sharing | Public profile = attack surface |
| Byte | LinkedIn Privacy in 2 Minutes | Action step |
| Course | Incident Response: First 30 Minutes | Executives are in the escalation path |
| Byte | Travel Security Checklist | Frequent travel = frequent exposure |
| **Total** | **4 courses + 3 bytes** | **~33 min** |

#### New Hire Onboarding
| Type | Item | Why |
|---|---|---|
| Byte | Your Company's Security Policy | Day 1: know where to look |
| Byte | Create a Passphrase in 60 Seconds | Day 1: set up credentials securely |
| Byte | Turn On MFA | Day 1: enable MFA, in the order the byte gives |
| Byte | The 5-Second Email Check | Day 1: immediate phishing defense |
| Byte | The Clean Desk Checklist | Day 1: physical security from the start |
| Course | Security Basics: Why One Setting Matters | Week 1: understand why this matters |
| Course | Social Engineering: How People Get Played | Week 1: recognize social engineering |
| Course | Physical Security: Desks, Screens, Printers | Week 1: physical security habits |
| Course | Phishing: Spot, Check, Report | Week 2: phishing recognition |
| Course | Incident Response: First 30 Minutes | Week 2: know what to do if something happens |
| **Total** | **5 courses + 5 bytes** | **~47 min** |

---

### Event-Triggered Assignments

Assign specific content automatically based on real events or simulation results.

| Trigger | Assign | Time |
|---|---|---|
| Failed phishing simulation | Byte: The 5-Second Email Check + Course: Phishing: Spot, Check, Report | 10 min |
| Reported phishing (positive behavior) | Thank-you message only | 0 min |
| Lost or stolen device | Byte: What to Do When You Lose Your Phone | 2 min |
| Data sharing incident | Course: File Sharing & Access + Byte: Is This PII? | 8 min |
| AI policy violation | Course: AI Tools: Safe Use at Work + Byte: How to Anonymize a Prompt | 9 min |
| New employee starts | Onboarding path (above) | 30 min |
| Pre-business travel | Byte: Travel Security Checklist | 2 min |
| Repeat offender (2+ simulation failures) | Full path starting from the relevant course | Varies |

---

### Seasonal Calendar (12-month drip)

One item per month, aligned with seasonal risk patterns.

| Month | Item | Type | Timing rationale |
|---|---|---|---|
| Jan | Course: Security Basics: Why One Setting Matters | Course | New year, fresh start |
| Jan | Byte: Check If You've Been Breached | Byte | Immediate action after foundation |
| Feb | Course: Social Engineering: How People Get Played | Course | Social engineering awareness |
| Mar | Course: Phishing: Spot, Check, Report | Course | Tax season = peak phishing |
| Mar | Byte: The 5-Second Email Check | Byte | Daily habit reinforcement |
| Apr | Course: Physical Security: Desks, Screens, Printers | Course | Spring cleaning — physical + digital |
| May | Course: AI Tools: Safe Use at Work | Course | Align with AI policy rollouts |
| May | Byte: How to Anonymize an AI Prompt | Byte | Summer intern onboarding |
| Jun | Course: Passwords & Passphrases | Course | Credential hygiene mid-year |
| Jul | Byte: Travel Security Checklist | Byte | Summer travel peak |
| Aug | Course: Laptop Security Settings + Your Phone | Course | Pre-vacation device check |
| Sep | Course: Social Media: What You're Really Sharing | Course | Back-to-work social audit |
| Oct | Byte: LinkedIn Privacy in 2 Minutes | Byte | EU Cybersecurity Month |
| Nov | Course: Incident Response: First 30 Minutes | Course | Year-end incident prep |
| Dec | Byte: STOP · DOCUMENT · REPORT Card | Byte | Holiday skeleton crew |

**Total: 9 courses + 6 bytes = ~75 min spread over 12 months (~6 min/month)**

---

## NIS2 / DORA Compliance Mapping

For EU organizations subject to NIS2 Directive Article 21(2) or DORA requirements.

| Requirement | Defence Lab coverage |
|---|---|
| NIS2 Art. 21(2)(a) — Risk analysis and security policies | Course 1 (Foundation), Course 11 (Data Classification: Four Levels) |
| NIS2 Art. 21(2)(b) — Incident handling | Course 13 (Incident Response: First 30 Minutes), Byte 13a (STOP/DOC/REPORT) |
| NIS2 Art. 21(2)(d) — Supply chain security | Course 12 (File Sharing & Access), Byte 12a (Sharing Files Safely) |
| NIS2 Art. 21(2)(g) — Basic cyber hygiene and training | All courses — especially General Awareness group (1-3) |
| NIS2 Art. 21(2)(g) — Phishing awareness | Course 6 (Phishing: Spot, Check, Report), Byte 6a (5-Second Email Check), Byte 6c (Report Phishing) |
| NIS2 Art. 21(2)(g) — Access control / credentials | Course 4 (passwords and MFA), Bytes 4a and 4b |
| NIS2 Art. 21(2)(j) — Cryptography and encryption | Course 7 (Laptop Security Settings) |
| DORA Art. 13.6 — ICT security awareness | All courses, role-based paths |
| DORA Art. 13.6 — Digital operational resilience training | Course 13, Course 1 |
| NIS2 Art. 20 — Management body training | Executive path |
| ISO 27001 Clause 7.2 — Role-based competence | Role-based learning paths |
| GDPR Art. 39.1(b) — Staff awareness | Courses 11-12 (Data Protection), Byte 11b (Is This PII?) |

---

## LMS Metadata Tags (per item)

Each item ships with the following tags for LMS filtering and automation:

| Tag category | Values |
|---|---|
| **Format** | `course` · `bite` |
| **Topic** | `passwords` · `mfa` · `phishing` · `devices` · `social-media` · `ai-security` · `data-protection` · `incident-response` · `privacy` · `travel` · `policy` |
| **Compliance** | `nis2` · `dora` · `iso27001` · `gdpr` · `pci-dss` · `hipaa` |
| **Role** | `all` · `finance` · `engineering` · `marketing` · `hr` · `executive` · `new-hire` |
| **Trigger** | `onboarding` · `refresher` · `incident-response` · `simulation-failure` · `seasonal` · `policy-change` |
| **Difficulty** | `foundational` · `intermediate` |

---

## Technical Specs

| Property | Value |
|---|---|
| Format | Self-contained HTML files |
| Hosting | Cloudflare Pages (or any static host) |
| State | localStorage (progress, action plan, XP) |
| LMS integration | LMS test is the compliance gate; courses are learning resources |
| Assessment | Quizzes inside courses are formative (learning checkpoints). LMS test is summative (compliance gate). |
| Accessibility | Keyboard navigation, ARIA labels, `prefers-reduced-motion` support, minimum contrast ratios |
| Languages | English (additional languages on request) |
| Device support | Desktop + mobile responsive |

---

## Appendix: Content Examples

### Example Course — "Phishing: Spot, Check, Report" (Course 6, ~8 min)

**S01 · Story (dark background)**
> Tag: TRUE STORY
> Title: The Friday Afternoon Email
>
> It's 4:47 PM on a Friday. Tom, an accountant, gets an email from his CEO asking for a $280,000 wire transfer. The email looks right — correct name, proper format, familiar signature. It even references a board meeting Tom presented at earlier that week.
>
> Tom hesitates. But the CEO is traveling, the timing makes sense, and he doesn't want to bother her. He processes the transfer at 4:52 PM.
>
> *Monday morning, the CEO knows nothing about any transfer. The money is gone.*

**S02 · Early win**
> Micro-check: Hover over any link in your inbox right now. See the real URL at the bottom of the screen? You just did the #1 phishing check. (+2 XP)

**S03 · Content — Four triggers**
> Almost every phishing message uses at least one of these:
> - ⏰ Urgency — "Your account will be closed in 24 hours"
> - 👔 Authority — "This is from the CEO"
> - 😨 Fear — "Suspicious activity on your account"
> - 🎁 Curiosity — "You have an unclaimed package"
>
> *Expandable accordions with examples for each.*

**S04 · Content — Types of phishing**
> Email, SMS (smishing), voice (vishing), QR codes (quishing).
> *One accordion per type, real-world examples.*

**S05 · Quiz (wager mechanic)**
> You get an email: "Your company email password expires today. Click here to renew or lose access by 5 PM." What trigger is this using?
>
> A) **Urgency + fear — act now or face consequences** ✅
> B) Authority — it claims to be from a powerful person
> C) Curiosity — it makes you want to know more
> D) Reward — it promises something valuable to you
>
> *Wager: Sure ×3 / Pretty sure ×2 / Guessing ×1*
> *Wrong answer shows: "📎 Missed this? Review S03 (Four triggers)."*

**S06 · Breather (dark, animated)**
> Scene: "The Inbox" — five emails appear one by one. Four are normal. One has subtle differences — misspelled domain, urgent subject, generic greeting. Cursor hovers, reveals the flags, clicks "Report."
>
> *Caption: "It sat between four normal emails. The only differences were small."*

**S07 · Interactive — Spot the Threat**
> A phishing email mockup. Learner clicks suspicious elements:
> 1. `arnazon.com` — spoofed domain
> 2. "URGENT + IMMEDIATELY" — pressure
> 3. "Dear Valued Customer" — generic greeting
> 4. "24 hours" — artificial deadline
> 5. `amaz0n-verify.net` — fake URL
> 6. "Amazon Security Division" — fake department
>
> *Score: Found X / 6. "Show what I missed" button.*

**S08 · Interactive — Phishing or Legit? (drag to classify)**
> Six messages — drag each to ✅ Legitimate or ❌ Phishing.
> Feedback per drop explains the key signals.

**S09 · Content — What to do**
> 1. Pause — don't click, don't reply
> 2. Verify through a different channel
> 3. Report it
>
> *Expandable: "If you already clicked" — change password, disconnect, tell IT.*

**S10 · Reflection**
> "Open your inbox right now. Pick one email and list 3 things that prove it's legitimate — sender address, specific details, link destination."

**S11 · Action**
> ⚡ Set up your email's phishing report button.
> - [ ] Find the "Report phishing" button in your email
> - [ ] Know your IT security team's email
> - [ ] Check that your email shows full sender addresses
>
> *📌 "Add to my action plan" (shows on your summary card)*

**S12 · Summary**
> Takeaways:
> 1. Phishing uses urgency, authority, fear, and curiosity
> 2. Check sender, check link, verify through a different channel
> 3. AI makes phishing look perfect — grammar is no longer a signal
>
> Your action plan: *(auto-filled)*
>
> *Want just the action step? → "The 5-Second Email Check" (2 min)*

---

### Example Quick Action — "The 5-Second Email Check" (Quick action 8, ~2 min)

**S01 · Hook**
> 90% of cyberattacks start with an email. Three checks, five seconds, before you click anything.

**S02 · How — The 3 checks (visual)**
> **1. Check the sender**
> Display name can say anything. Tap/click to see the real address.
> *Visual: "Amazon Security" → actual address `security@arnazon.com` (rn ≠ m)*
>
> **2. Check the link**
> Desktop: hover without clicking. Phone: long-press.
> *Visual: link text says "amazon.com/verify" → real URL is `amaz0n-secure.net/login`*
>
> **3. Check the tone**
> Generic greeting + artificial deadline + threat = red flag.
> *Visual: "Dear Customer, verify within 24 hours or your account will be closed"*

**S03 · Do it — Practice**
> Try it now. Open your inbox. Pick any email with a link.
> - [ ] Check the sender's full address
> - [ ] Hover/long-press one link — see where it goes
> - [ ] Spot the tone: is there urgency or pressure?
>
> (+2 XP)

**S04 · Done**
> That's the 5-second check. Sender, link, tone.
> Do it once consciously and it becomes automatic.
>
> *Want the full story behind this? → "Phishing: Spot, Check, Report" (8 min)*

---

## AI Buddy — Personalized Practice Blocks

Optional AI-powered practice blocks in select courses. Each appears after the main content, before the summary. Explicit opt-in with disclosure.

**Opt-in UI:**
> 🤖 **Practice with AI** *(optional)*
> This exercise uses AI to give you personalized feedback. No data is stored or shared.
> [Try it] · [Skip]

**Technical stack:** Cloudflare Pages (HTML) → Cloudflare Worker (API proxy, holds key) → Claude API. No storage, no database. Image and text sent, analyzed, response returned, nothing persisted.

---

### By format

#### 📨 Text analysis — "paste it, I'll check it"

Student pastes real content from their work. AI analyzes and gives specific, actionable feedback.

| Course | Prompt to student | What AI does |
|---|---|---|
| **Phishing: Spot, Check, Report** | "Paste a suspicious email (or any email) — I'll check it" | Analyzes sender address, URLs, tone, triggers. Flags what's suspicious and why. If clean — explains what made it trustworthy. |
| **Social Media: What You're Really Sharing** | "Paste a LinkedIn post or describe a photo you're about to share" | Shows what an attacker would extract: software names, travel plans, org structure, location data. Suggests a safer version. |
| **AI Tools: Safe Use at Work** | "Paste your last AI prompt — I'll run the billboard test" | Checks for client names, internal data, credentials, project details. Returns an anonymized version of the same prompt that gets the same result without the exposure. |
| **File Sharing & Access** | "Describe how you just shared a file — who, what platform, what settings" | Checks: is the sharing method appropriate for the classification level? Flags "anyone with the link" on confidential data, missing expiry dates, folder inheritance risks. |

#### 📸 Image analysis — "upload a photo, I'll spot the risks"

Student uploads a photo. AI uses vision to identify security issues.

| Course | Prompt to student | What AI does |
|---|---|---|
| **Physical Security: Desks, Screens, Printers** | "Take a photo of your desk right now — I'll spot what an attacker would see" | Identifies: visible passwords on sticky notes, unlocked screens, sensitive documents left out, badge visible, whiteboard content, monitor angled toward foot traffic. Gives a risk score and specific fixes. |
| **Social Media: What You're Really Sharing** | "Upload a team photo before you post it" | Flags: visible whiteboards, software on screens, badge details, office layout clues, anything that reveals internal tools or projects. Alternative to text analysis — same course, learner chooses format. |

#### 🎭 Role-play — "I'll pretend to be the attacker"

AI plays a character. Student responds in real time. AI gives feedback on their decisions.

| Course | Scenario | What AI does |
|---|---|---|
| **Social Engineering: How People Get Played** | "You get a call from IT support asking for your credentials to fix a critical issue" | AI plays the social engineer — uses urgency, authority, technical jargon. Adapts based on student's responses. If student gives info → explains what went wrong. If student resists → confirms correct instinct and shows what the attacker would try next. |
| **Phishing: Spot, Check, Report** | "Your CEO messages you on Teams asking for a quick favor" | AI plays a BEC attacker. Escalates pressure if student pushes back. Tests whether student verifies through a separate channel. |

#### 🏋️ Coaching — "describe your situation, I'll walk you through it"

Student describes a real or hypothetical scenario. AI guides them through the correct response framework.

| Course | Prompt to student | What AI does |
|---|---|---|
| **Incident Response: First 30 Minutes** | "Describe something that happened (or invent a scenario) — I'll coach you through the response" | Walks through STOP/DOCUMENT/REPORT for their specific case. What to stop doing, what to document (with specific questions), who to call and what to say. Adapts to incident type. |
| **Data Classification: Four Levels** | "Describe a file or dataset you work with — I'll help you classify it" | Asks clarifying questions (who has access? is there PII? is it under regulation?). Returns classification level (Public/Internal/Confidential/Restricted) with reasoning. |

#### 🔐 Strength check — "show me your pattern, I'll test it"

Student describes their approach (not actual credentials). AI evaluates and improves.

| Course | Prompt to student | What AI does |
|---|---|---|
| **Passwords & Passphrases** | "Describe your password pattern — don't type a real password, just the pattern (e.g. 'word + number + symbol')" | Estimates crack time for the pattern. Explains why it's strong or weak. Generates 3 passphrase alternatives following the course's method. Shows the math comparison. |

---

### Summary: AI Buddy coverage

| Course | Format | AI Block |
|---|---|---|
| Security Basics: Why One Setting Matters | — | No AI block (foundational, no grey-zone skill) |
| **Social Engineering: How People Get Played** | 🎭 Role-play | AI plays social engineer, student responds |
| **Physical Security: Desks, Screens, Printers** | 📸 Image | Upload desk photo, AI spots risks |
| **Passwords & Passphrases** | 🔐 Strength check | Describe pattern, AI estimates crack time |
| **Phishing: Spot, Check, Report** | 📨 Text + 🎭 Role-play | Paste email for analysis, or BEC role-play |
| Laptop Security Settings | — | No AI block (checklist-based) |
| Phone Security Settings | — | No AI block (checklist-based) |
| **Social Media: What You're Really Sharing** | 📨 Text + 📸 Image | Paste post or upload photo for attacker-view analysis |
| **AI Tools: Safe Use at Work** | 📨 Text | Paste prompt, get billboard test + anonymized version |
| **Data Classification: Four Levels** | 🏋️ Coaching | Describe a file, AI classifies it with reasoning |
| **File Sharing & Access** | 📨 Text | Describe sharing setup, AI checks appropriateness |
| **Incident Response: First 30 Minutes** | 🏋️ Coaching | Describe incident, AI walks through STOP/DOC/REPORT |

**9 out of 13 courses have AI blocks.** 4 don't need them (foundational or checklist-based).

**5 distinct formats:** text analysis, image analysis, role-play, coaching, strength check. No two consecutive courses use the same format — variety keeps engagement.

---

## Build status

Files are numbered by their catalogue number, not by the order they were built.
Format: all built items use the **scroll** engine — one continuous timeline of nodes,
each node gated by a spot (predict / quiz / experience / signature widget), followed by
a scene-2 checklist that assembles the learner's personal action plan.

| Catalogue # | Item | File | Status |
|---|---|---|---|
| Course 1 | Security Basics: Why One Setting Matters | `courses/01-security-basics.html` | Built as *How a Breach Unfolds*, ~6 min |
| Course 2 | Social Engineering: How People Get Played | `courses/02-social-engineering.html` | Built as *How People Get Talked Into It*, opens attacker-side. ~7 min base |
| Course 3 | Physical Security: Desks, Screens, Printers | `courses/03-physical-security.html` | Built as *Screens, Paper and Devices*, opens with a self-audit. ~4 min base, ~5 with the two deep-dive blocks expanded |
| Course 4 | Reused Passwords and the Second Lock | `courses/04-passwords-mfa.html` | Built, ~7 min — carries both passwords and MFA; the old Course 5 is folded in |
| Course 5 | MFA: The Second Step | — | **Dropped.** Course 4 covers passwords and the second step in one pass; splitting them would mean either removing MFA from Course 4 or repeating it. |
| Course 6 | Phishing: Spot, Check, Report | `courses/06-the-447-email.html` | Built as *Spotting a Fake Email*, cold-open email pick. ~6 min base, ~7 with deep dives |
| Byte 1b | Tools Worth Knowing About | `bytes/01b-security-toolkit.html` | Built |
| Course 7 | Laptop Security Settings | `courses/07-laptop-security.html` | Built as *What Runs on Your Laptop*, opens with a myth-buster. ~5 min |
| Course 8 | Phone Security Settings | `courses/08-phone-security.html` | Built as *What Your Phone Can Reach*, opens by weighing laptop against phone. ~5 min |
| Course 9 | Social Media: What You're Really Sharing | `courses/09-online-presence.html` | Built as *What You Post About Work*, opens by estimating how much one post gives away. ~5 min |
| Byte 2a | Your Verification Card | `bytes/02a-verification-card.html` | Built — adapts to org size; `ORG` block at the top lets a client pre-fill their own details |
| Byte 6b | Link Inspector | `bytes/06b-link-inspector.html` | Built |

Everything else in this catalogue is still to be produced.

### Opening variety

Courses should not all open with a true story — by the fifth one, learners anticipate the
scare and disengage. Openings rotate across: story, challenge / cold open, myth-buster,
self-audit, a single number, and "you are the attacker". No two consecutive courses in a
learning path use the same opening.

| Course | Opening used |
|---|---|
| 1 | Story — the $2.4B Change Healthcare breach |
| 2 | You are the attacker — pick the cheapest way in |
| 3 | Self-audit — look at the room you are in |
| 4 | Story — the domino effect |
| 6 | Challenge / cold open — two emails, pick the fake |
| 7 | Myth-buster — three beliefs about laptops, true or false |
| 8 | Weigh two options — laptop or phone, which costs you more |
| 9 | Estimate — guess how many useful details one post holds, then see them |

### Length and optional depth

Courses target **~8 minutes at the base layer**, measured at 200 words per minute across body
text, feedback, widget explanations and checklist steps.

Detail that is genuinely useful but not needed to act on the material goes into a collapsed
`more` block inside a node — not a separate node, so the timeline and the progress bar stay
the same length either way. Two or three per course at most. The label states what is inside
("Why the login screen stops mattering") rather than inviting the reader onward, so it reads
as optional depth rather than a truncated base layer.

| Course | Base | With depth expanded |
|---|---|---|
| 1 | ~6 min | — |
| 2 | ~7 min | ~7.5 min |
| 3 | ~4 min | ~5 min |
| 4 | ~7 min | — |
| 6 | ~6 min | ~7 min |
