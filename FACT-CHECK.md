# Defence Lab — реєстр перевірки фактів

Станом на 12 листопада 2026. Охоплює 8 побудованих курсів і 5 байтів.

Правило, за яким це зроблено: усе, що можна показати цитатою з джерела — лишається з джерелом; усе, що я знав «із пам'яті» і не підтвердив — або виправлено, або явно позначено як сценарій. Жодне твердження не лишилося у вигляді правдоподібного числа без умови.

---

## 1. Що виправлено

| Курс | Було | Стало | Чому |
|---|---|---|---|
| 01 | Співробітник Change Healthcare використовував робочий пароль на інших сайтах, один із них зламали | «Як саме облікові дані були отримані, публічно не розкривали» + звичайні маршрути як загальний патерн | Witty у свідченнях сказав лише «compromised credentials». Історію про повторне використання я вигадав |
| 01 | «Рахунок перевищує $2.4 млрд» — включно зі штрафами регуляторів і позовами | Власна оцінка UnitedHealth за 2024: **$2.3–2.45 млрд** | Цифра UNH — це витрати на відновлення й збій бізнесу, не штрафи й позови |
| 02 | «Захопили 130 акаунтів» | **~130 у цілі, 45 захоплено** | Офіційна заява Twitter розділяє ці два числа |
| 03 | «Новинна агенція… фото співробітника» | AP, фото від 21.07.2017, помічене в січні 2018; людина на фото не надсилала тривогу | Дата й атрибуція були відсутні; про чоловіка на фото писали окремо — його публічно звинувачували безпідставно |
| 03 | «Французький мовник у 2015» | TV5Monde, квітень 2015, наступного дня після атаки, пароль від YouTube-каналу | Конкретика перевіряється, узагальнення — ні |
| 03 | «За GDPR є загалом 72 години» | Дослівна норма ст. 33(1) + умови: персональні дані, «where feasible», виняток за низького ризику, обов'язок на організації | Класична втрачена умова: без неї твердження хибне для більшості читачів поза ЄС |
| 07, 08 | DEF CON 2019, точка доступу «Free Conference WiFi», сотні підключень | Справа AFP про «evil twin» мережі в аеропортах Перта, Мельбурна, Аделаїди та на внутрішніх рейсах, червень 2024 | Історію про DEF CON я не знайшов у жодному джерелі. Схоже на апокриф |
| 07 | «близько 147 мільйонів людей» | Те саме, але з атрибуцією FTC | Цифра правильна, джерело треба назвати |
| 08 | «У 2021 застосунок-ліхтарик з десятками мільйонів завантажень…» | Дослідження Avast, вересень 2019: 937 застосунків, у середньому 25 дозволів, максимум 77 | Конкретного застосунку 2021 року я не знайшов. Дослідження Avast — реальне, але це вендорське дослідження |
| 08 | «Пошкоджена зарядна точка може читати з телефона — FBI і FCC попереджали» | Те саме + **жодного підтвердженого реального випадку не зафіксовано** | Попередження справжні, але огляди фіксують відсутність підтверджених випадків поза дослідженнями |
| 08 | «Підказки "тільки заряджання" можна обійти на зламаному обладнанні» | ChoiceJacking, USENIX Security 2025, з назвою дослідження й статусом виправлень | Твердження виявилося правдивим, але я подав його без джерела — а воно потрібне, бо це свіже дослідження |
| 04 | «Менш ніж 3 години» для Tr0pical!2024, «близько 550 років» для парольної фрази | Механізм (словник + правила) замість чисел; числа лишилися тільки в слайдері, де вже є дисклеймер | Час злому залежить від хешу й заліза. Без цієї умови число — вигадка з виглядом точності |
| 04 | «Це трапляється близько 300 000 разів на день» | 193 млрд спроб credential stuffing у мережі Akamai за 2020 | 300 000/день я вигадав. Akamai — вендорський вимір власної мережі, це позначено |
| 04 | «Навіть якщо сервери менеджера зламають, дані марні» | Те саме + випадок LastPass 2022: сховища вивезли й ламали офлайн, слабкі майстер-паролі піддалися | Зайва категоричність |
| 06 | «Усі інші учасники дзвінка були синтетичні — згенеровані з публічно доступних записів керівників» | Названо Arup, HK$200 млн, 15 переказів; «як саме зробили фейки — не розкривали» | Про публічно доступні записи джерел немає |
| 06 | Том і $280 000 подані як випадок | Явна позначка: сценарій, зібраний із типового патерну | Зовнішнього джерела немає |
| 09 | «Як одне фото команди стало сценарієм шахрайства на $340 000» | Та сама позначка про сценарій, підзаголовок без суми | Те саме |

Додатково: посилання на NIST вели на `sp800-63b.html`, якого немає — замінено на живий розділ `sp800-63b/authenticators`.

У кожен курс додано згортний блок **«Sources and what is not sourced»** у фінальній картці: перелік джерел і окремо те, що джерелами не підтверджене.

---

## 2. Таблиця джерел

| № | Повна адреса | Що підтверджує | Рівень | Як знайдено | Дата |
|---|---|---|---|---|---|
| 1 | https://www.healthcaredive.com/news/change-healthcare-compromised-credentials-no-mfa/714824/ | Прямі цитати зі свідчень Witty: «compromised credentials», «The portal did not have multifactor authentication», «Ransomware was deployed nine days later»; перший доступ 12 лютого | 3 (цитує рівень 1 — письмові свідчення) | пошук «Witty Senate testimony Change Healthcare Citrix no MFA» | 30.04.2024 |
| 2 | https://www.secureworld.io/industry-news/unitedhealth-change-healthcare-attack-costs | «total cost of the breach to be between $2.3 billion and $2.45 billion in 2024», за пресрелізом UNH Q2 2024 | 3 | пошук про вартість атаки | 18.07.2024 |
| 3 | https://www.sec.gov/Archives/edgar/data/731766/000073176624000323/unh-20240930.htm | Форма 10-Q UnitedHealth за Q3 2024 — первинне джерело для цифр | 1 | у результатах пошуку | Q3 2024 |
| 4 | https://www.npr.org/2020/07/18/892615413/we-re-embarrassed-twitter-says-high-profile-hack-hit-130-users | ~130 акаунтів у цілі; інші джерела того ж дня додають 45 захоплених | 3 | пошук «Twitter 130 accounts targeted» | 18.07.2020 |
| 5 | https://www.npr.org/2020/07/31/897815039/florida-teen-charged-as-mastermind-of-massive-twitter-hack | Звинувачення, 31.07.2020 | 3 | той самий пошук | 31.07.2020 |
| 6 | https://www.cbsnews.com/minnesota/news/password-for-hawaiian-alert-agency-kept-on-post-it-note | Пароль на стікері в опублікованому фото агенції Гаваїв | 3 | пошук «Hawaii emergency management password post-it AP photo» | січень 2018 |
| 7 | https://www.businessinsider.in/tech/a-password-for-the-hawaii-emergency-agency-was-hiding-in-a-public-photo-written-on-a-post-it-note/articleshow/62531465.cms | Підпис до фото: **п'ятниця, 21 липня 2017**; чоловік на фото — Jeffrey Wong, operations officer; комп'ютери на фото «likely different from the system that sent the false missile alert» | 3 | той самий пошук | січень 2018 |
| 8 | https://www.csoonline.com/article/2908852/hacked-french-broadcasters-passwords-revealed-in-tv-broadcast.html | TV5Monde, паролі видно в інтерв'ю, зокрема від YouTube | 3 | пошук «TV5Monde passwords on wall interview» | квітень 2015 |
| 9 | https://gdpr-text.com/uk/read/article-33 | Ст. 33(1): «In the case of a personal data breach, the controller shall without undue delay…»; «unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons» | 1 (текст регламенту) | пошук тексту статті | чинна редакція |
| 10 | https://www.hipaajournal.com/6-9-million-23andme-users-affected-by-data-breach/ | ~14 000 акаунтів через credential stuffing, 6,9 млн зачеплених через DNA Relatives | 3 | пошук «23andMe 14000 accounts 6.9 million» | грудень 2023 |
| 11 | https://www.darkreading.com/cloud-security/credential-stuffing-reaches-193-billion-login-attempts-annually | 193 млрд спроб credential stuffing у мережі Akamai за 2020 | 3 (переказ рівня 2 — звіту Akamai) | пошук «Akamai credential stuffing billions» | 2021 |
| 12 | https://pages.nist.gov/800-63-4/sp800-63b/authenticators | §3.1.1.2: мінімум 15 символів для однофакторних, 8 для багатофакторних; «SHALL NOT impose other composition rules»; «SHALL NOT require subscribers to change passwords periodically» | 1 | заміна непрацюючого посилання | SP 800-63-4 |
| 13 | https://www.insurancebusinessmag.com/asia/news/cyber/deepfake-video-conference-sees-criminals-escape-with-hk200-million-489791.aspx | 15 переказів на HK$200 млн; працівник підозрював фішинг в початковому листі; поліція (Baron Chan Shun-ching): усі, кого він бачив на дзвінку, були підробкою | 3 | пошук «Arup deepfake Hong Kong police» | лютий 2024 |
| 14 | https://help.dropbox.com/accounts-billing/security/official-domains | dropboxmail.com — справжній домен відправки Dropbox: «All promotional and tip emails originate from docsend.com, dropboxmail.com, em-s.dropbox.com» | 1 | пошук за доменом | поточна версія |
| 15 | https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach | «affected approximately 147 million people»; «failed to patch its network after being alerted in March 2017» | 1 | пошук «FTC Equifax settlement» | 22.07.2019 |
| 16 | https://9to5google.com/2021/02/04/the-great-suspender-extension-has-been-removed-from-chrome-web-store-for-containing-malware/ | The Great Suspender прибрано з Chrome Web Store за шкідливий код після зміни власника | 3 | пошук «Great Suspender removed malware» | 04.02.2021 |
| 17 | https://afp.gov.au/news-centre/media-release/man-charged-over-creation-evil-twin-free-wifi-networks-access-personal | «evil twin» мережі в аеропортах Перта, Мельбурна, Аделаїди та на внутрішніх рейсах; «they were taken to a fake webpage requiring them to sign in using their email or social media logins»; «dozens of personal credentials belonging to other people» | 1 (пресреліз поліції) | пошук «AFP evil twin wifi airport» | 28.06.2024 |
| 18 | https://en.wikipedia.org/wiki/Juice_jacking | «multiple reviews have found no credible reported cases of juice jacking on mobile OSs outside of research efforts»; попередження FBI Denver 06.04.2023 і оновлене FCC | 3 (з посиланнями) | пошук «juice jacking FBI FCC no confirmed cases» | поточна версія |
| 19 | https://www.usenix.org/conference/usenixsecurity25/presentation/draschbacher | ChoiceJacking: перша атака, що обходить підказку підтвердження USB-з'єднання; пристрої 8 вендорів, зокрема топ-6; Google, Samsung, Xiaomi, Apple підтвердили й впроваджують пом'якшення | 1 (оригінальна публікація) | пошук «ChoiceJacking USENIX 2025» | серпень 2025 |
| 20 | https://www.securityweek.com/android-flashlight-apps-request-77-permissions/ | Avast: 937 застосунків-ліхтариків, у середньому 25 дозволів, максимум 77; 180 просять контакти, 77 — запис аудіо | 3 (переказ рівня 2 — дослідження Avast) | пошук «flashlight app permissions study» | 13.09.2019 |

---

## 3. Твердження, які має підтвердити людина

1. **$22 млн викупу Change Healthcare (курс 1).** Цифра з преси й з блокчейн-аналітики, не з подання компанії. Перевірити, чи влаштовує такий рівень джерела.
2. **«Торкається приблизно одного з трьох записів пацієнтів у США» (курс 1).** Формулювання взяте зі свідчень Witty у переказі. Перевірити точне формулювання у письмових свідченнях — там є різні варіанти («one in three patient records», «15 billion transactions»).
3. **«Зловмисники читали пошту компанії тижнями» (курс 6, сценарій Тома).** Це типовий патерн BEC, не факт конкретної справи. Якщо хочеш, можна прив'язати до звіту FBI IC3 — я його не перевіряв.
4. **Статус справи AFP (курси 7, 8).** Я знайшов пресреліз про звинувачення (червень 2024). У пошуку трапився заголовок про вирок («Australian Man Jailed»), але я його не відкривав і не підтверджував. Якщо хочеш писати «засуджений», це треба перевірити окремо.
5. **Статус виправлень ChoiceJacking (курс 8).** На серпень 2025 вендори «in the process of integrating mitigations». Чи закрито це зараз на iOS та Android — я не перевіряв.
6. **Назви й поведінка інструментів у байті 01b (Security toolkit).** Я не перевіряв жоден із перелічених продуктів на актуальність: чи існує, чи безкоштовний, чи робить те, що написано. Для списку інструментів це найшвидше старіє.
7. **Шляхи в налаштуваннях у всіх чеклістах** («Settings → Privacy & Security → …»). Вони змінюються з кожною версією iOS, Android, LinkedIn і Google. Жоден я не відкривав і не звіряв.

---

## 4. Де я не впевнений

- **Історія про DEF CON 2019 — я її не знайшов, але й не спростував.** Я шукав чотирма формулюваннями; знайшлися RSA Conference 2016, DEF CON 30 (2022) і Wall of Sheep, але не «Free Conference WiFi» 2019. Можливо, вона існує в джерелі, до якого я не дійшов. Я її прибрав, бо не можу показати цитату — а не тому, що довів її хибність.
- **Застосунок-ліхтарик 2021 року.** Те саме: не знайшов. Замінив на дослідження Avast, яке знайшов.
- **Чи змінений був пароль на фото з Гаваїв.** Заяву агенції я не знайшов. Прибрав це речення.
- **Скільки рахунків отримали гроші Arup.** CNN і SCMP писали про п'ять місцевих рахунків, але джерело, яке я відкрив, цього не підтверджує. У тексті курсу цього числа більше немає.
- **Рівень джерел для Twitter 2020.** Оригінальна заява Twitter у блозі мені не відкрилася; я спираюся на репортаж того ж дня. Це переказ, не першоджерело.
- **Akamai 193 млрд — це 2020 рік.** Цифра стара й вендорська. Вона в тексті підписана, але якщо курс житиме ще рік, її варто або оновити, або прибрати.
- **GDPR поза ЄС.** Я додав речення про те, що в інших юрисдикціях строк інший, але не перевіряв жодного конкретного закону. Якщо аудиторія українська — варто звірити з українським законом про захист персональних даних окремо, я цього не робив.

---

## 5. Різні назви того самого

- **Evil twin / rogue access point / fake hotspot / honeypot WiFi** — у курсах вживається «evil twin» з поясненням. У джерелах зустрічаються всі чотири.
- **Juice jacking / USB charging attack / ChoiceJacking.** Перші два — те саме явище; ChoiceJacking — конкретна атака 2025 року, яка обходить захист від першого. Це не синоніми, і в тексті вони розведені.
- **Credential stuffing / password spraying.** Часто плутають. Stuffing — відомі пари логін+пароль з інших витоків проти багатьох сайтів; spraying — один поширений пароль проти багатьох акаунтів. У курсі 4 вживається тільки перше, і це правильно для описаного сценарію.
- **MFA / 2FA / two-step verification.** У курсах усюди MFA. Вендори називають це по-різному в налаштуваннях, і в чеклістах це варто згадувати.
- **BEC / CEO fraud / invoice fraud / whaling.** Сценарії в курсах 6 і 9 — це BEC. Жоден із цих термінів у тексті не вжито; якщо вони потрібні в глосарії програми, їх треба додати узгоджено.
- **Passphrase / парольна фраза / passkey.** Passkey — це зовсім інше (безпарольний другий фактор), і в байті 01b воно згадується поруч із passphrase. Варто перевірити, що читач їх не сплутає.
