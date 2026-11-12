const NODES=[
 {date:'Start here',crit:0,beat:'Put the first four actions in order',
  body:'You opened an attachment from a supplier you deal with every week. A window flashed and closed. A minute later, filenames in your documents folder are changing on their own.<br><br>Four things need doing. <b>Tap them in the order you would actually do them</b> — the order is the whole question here, not the list.',
  spot:{type:'order',topic:'order',
    scenario:'Files are renaming themselves on your laptop, right now.',
    items:[
     {t:'Write down the time and what you opened',
      why:'Third. It matters — you are the only person who knows what you clicked and when — but it takes minutes you do not have while the thing is still spreading. Do it while you wait for someone to arrive.'},
     {t:'Turn off the WiFi, or unplug the network cable',
      why:'First, and it is not close. Everything else can wait sixty seconds; this is the only step that stops the problem reaching shared drives and colleagues. CISA’s ransomware guidance puts isolating the affected machine first too.'},
     {t:'Leave the laptop switched on and hand it over',
      why:'Last. Instinct says shut it down, and shutting down throws away evidence held in memory that will not exist again. Disconnected and running is what you want to hand over.'},
     {t:'Tell whoever handles this — IT, your manager, the owner',
      why:'Second. Once it cannot spread, the next scarcest thing is someone who can act. Telling them takes thirty seconds and starts everything that follows.'}],
    order:[1,3,0,2],
    fb:'Disconnect, tell someone, write it down, hand it over running.<br><br>Two of these go wrong routinely. People <b>shut the machine down</b>, because that feels like stopping it — and it destroys what was in memory. And people <b>write the whole account first</b>, because that feels responsible — while the thing is still reaching the shared drive.<br><br>The order is not a ritual. Each step is ordered by what it stops you losing: first the spread, then the time, then the detail, then the evidence.'}},

 {date:'The real delay',crit:1,beat:'Most of the damage happens while nobody has said anything',
  body:'That was the easy version, because you knew something was wrong.<br><br>The expensive version is quieter. Someone clicks a link, types their password into a page that turns out to be fake, and realises about an hour later. Nothing is visibly broken. And then they do not tell anyone — not out of carelessness, but because telling someone means saying out loud that they fell for it.<br><br>The UK’s National Cyber Security Centre puts it plainly: <b>“the stigma of clicking can prevent people reporting it, which then delays the incident response.”</b> The click is not what costs money. The hours of silence after it are.',
  more:{t:'Why the blame reflex is treated as an organisational fault, not a personal one',
    body:'The NCSC’s position is that an organisation which responds to clicks with blame has chosen slow incident response, and it names what to stop doing: “It’s time for organisations to move away from using blame and fear around clicking links”, and specifically not running phishing exercises that chastise people for clicking.<br><br>Their argument is that catching every convincing message was never a realistic thing to ask of a person, so the defences that actually hold are technical — filtering, DMARC, EDR — and the thing people <i>are</i> uniquely good at is noticing that something felt wrong and saying so quickly.<br><br>Which means the useful question after an incident is not “who clicked”. It is how long it took to hear about it, and what made that number what it was.'},
  spot:{type:'predict',topic:'delay',q:'You think you entered your password on a fake page about an hour ago. Nothing looks broken. What now?',
    opts:[
     ['Tell someone now, and say you are not certain',1],
     ['Check your accounts first, so you can report properly',0],
     ['Change the password and see if anything happens',0]],
    fb:'Now, uncertainty included. “I think I may have put my password into a fake page, I am not sure” is a complete and useful report.<br><br>Checking first feels more responsible and costs the hour that matters — and you cannot see most of what a responder can. Changing the password is worth doing, but it is not instead of telling someone: if the account has already been used, the person who can see that is not you.'}},

 {date:'Do not tidy',crit:1,beat:'The instinct to clean it up destroys what is needed',
  body:'There is a second reflex, and it comes from the same place as the silence: make it go away before anyone sees.<br><br>So the email gets deleted. The downloaded file gets dragged to the bin. The machine gets restarted, or wiped and set up again. Each one feels like fixing it. Each one removes something the person investigating needs — and none of them undo anything that already happened.',
  spot:{type:'quiz',topic:'evidence',q:'You reported a suspicious email. While waiting, what do you do with it?',
    opts:[
     ['Leave it exactly where it is',1],
     ['Delete it so nobody opens it by accident',0],
     ['Forward it to colleagues as a warning',0],
     ['Move it to a folder to keep it tidy',0]],
    fb:'Leave it. The headers are how anyone works out where it came from, who else got it, and whether it slipped past filtering — and that is gone once it is deleted.<br><br>Forwarding spreads a live link to more people, and a warning that quotes the subject line does the same job safely. Moving it is usually harmless and occasionally not, because some rules act on folders.'}},

 {date:'If there is nobody',crit:0,beat:'Who to tell when no one handles this where you work',
  body:'All of that assumes somebody to tell. Plenty of people have no IT department — small firms, sole traders, contractors working in a client’s systems.<br><br>That changes who, not what. Disconnect still comes first. Reporting becomes reporting outward: the bank if money is involved, the client if it is their systems, your provider if it is their service, and the national reporting line in your country.',
  more:{t:'Two situations where reporting outward has its own clock',
    body:'<b>Money has moved.</b> Ring the bank on the number printed on your card, not one from any message, and say the word <i>fraud</i>. Recovery depends on how fast the receiving bank can be contacted, which is measured in hours.<br><br><b>Personal data may be involved.</b> If you handle data about other people and it may have been exposed, there is likely a legal reporting duty with a deadline attached — 72 hours from awareness under the GDPR, and something comparable in most other regimes. The clock starts when someone becomes aware, which is one more reason the hour of silence is expensive.<br><br>If you work inside a client’s systems, their rules apply to their systems. Finding out who to call <i>there</i> is a question for a quiet afternoon, not for the afternoon it happens.'},
  spot:{type:'experience',topic:'who',q:'If something went wrong in the next ten minutes, do you know who you would tell?',
    scale:['Yes, by name','Roughly','Not really'],
    note:'“Roughly” and “not really” are the common answers, and they are the ones that turn into the hour of silence — because when it happens you are not calmly looking up a process, you are rattled and hoping it resolves itself.<br><br>Name is enough. One person, and a way to reach them that does not depend on the thing that broke: if it is your laptop or your email that is compromised, a phone number matters more than a chat handle.'}},

 {scene2:1,date:'Your plan',crit:0,beat:'Three things to settle before you need them',
  body:'Mark whichever you mean to do.',
  spot:{type:'checklist',
    items:[
      {topic:'who',t:'Write down who you would tell, and how to reach them',
       how:'Decide it now, because the moment it happens is the worst moment to work it out.',
       steps:['Name one person or team, and a second if the first is unreachable','Keep a phone number, not only a chat handle — the compromised thing may be your email','If you work in a client’s systems, find out who to call on their side as well'],
       itnote:'If your organisation has an incident process, the answer is in it. Worth reading once while nothing is happening.'},
      {topic:'order',t:'Learn the order, not the details',
       how:'Four steps, and the order is what makes them work: disconnect, tell someone, write it down, hand it over running.',
       steps:['Disconnect first — it is the only step that stops it spreading','Tell someone second, uncertainty included','Write down the time and what you did while you wait','Leave the machine on; shutting it down throws away evidence'],
       itnote:''},
      {topic:'delay',t:'Decide now that you will report before you are sure',
       how:'The hour spent checking whether it is real is the hour that costs money.',
       steps:['“I think I may have — I am not certain” is a complete report','A false alarm costs someone ten minutes; silence costs hours nobody gets back','If reporting a mistake is treated badly where you work, that is a fault in the workplace, not a reason to stay quiet'],
       itnote:''}
    ]}}
];
