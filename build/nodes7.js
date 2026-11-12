const NODES=[
 {date:'Start here',crit:0,beat:'Three things people believe about laptops',
  body:'All three sound reasonable. All three are wrong, and each one is wrong in a way that matters. Decide on each before you open it.',
  spot:{type:'myths',topic:'belief',
    items:[
     {t:'“My laptop has a password, so my files are safe if it is stolen.”',truth:0,
      why:'A password protects the operating system. Take the drive out, connect it to another computer, and there is no login to pass — the files are simply there. Only <b>full-disk encryption</b> changes that.'},
     {t:'“My antivirus will catch anything dangerous.”',truth:0,
      why:'Antivirus catches what it recognises. It is a useful floor, not a ceiling — and one of the first things malware does is switch it off. An antivirus that will not stay on is not a glitch; it is a symptom.'},
     {t:'“Updates can wait until it is convenient.”',truth:0,
      why:'The moment a patch is published, its contents become a public description of the hole it fixes. Attackers read patches and scan for machines that have not installed them. Waiting a week is not neutral — it is the week they are looking.'}],
    fb:'The pattern is the same in all three: the protection people assume they have is doing something narrower than they think.<br><br>What follows is the three that actually carry weight on a laptop — and none of them need you to be technical.'}},

 {date:'Updates',crit:1,beat:'A patch is also a map for attackers',
  body:'That last myth has a famous example. In 2017 Equifax knew about a vulnerability in software they ran, the patch existed, and it was not applied. Attackers used that exact hole and took the personal records of about 147 million people.<br><br>Nobody was tricked. Nobody clicked anything. A known fix was available and sitting uninstalled.',
  more:{t:'Why the gap after a patch is the dangerous part',
    body:'When a vendor publishes a security update, it usually publishes what it fixed — a reference number and a description. Security researchers need that. So do attackers, who work backwards from the description to build something that exploits machines where the patch has not landed yet.<br><br>The window between “patch released” and “patch installed” is therefore the most dangerous period in a vulnerability’s life, not the quiet months before anyone noticed. Automatic updates matter because they close that window without needing you to decide anything at the moment you are busiest.'},
  spot:{type:'quiz',topic:'updates',q:'When is a known vulnerability most dangerous to your machine?',
    opts:[
     ['Before anyone has discovered it exists',0],
     ['In the days right after the fix is published',1],
     ['Years later, once the software is out of support',0],
     ['Only if you use the software every day',0]],
    fb:'Right after the fix comes out. The patch notes describe what was broken, which gives attackers a starting point and a reason to hurry. Unsupported software is genuinely risky too, but the sharp spike is in the days following a release.'}},

 {date:'Extensions',crit:0,beat:'What your browser add-ons can read',
  body:'Updates are the part you can automate. This one you have to look at.<br><br>Browser extensions run with broad permissions: many can see what you type, which sites you visit and what you download. That is often what makes them useful.<br><br>They can also change hands. “The Great Suspender” was a popular Chrome extension until it was sold; the new owner added code that tracked users. Nothing changed on screen, and it updated itself silently like any other extension.',
  spot:{type:'quiz',topic:'extensions',q:'You have eight extensions installed and use two of them. What is the right move?',
    opts:[
     ['Keep them all — unused extensions are inactive anyway',0],
     ['Check the reviews on the six you do not use',0],
     ['Remove the six you do not use',1],
     ['Disable the six but leave them installed',0]],
    fb:'Remove them. An unused extension is not inactive — it still has its permissions and still updates itself, including into the hands of a new owner. Reviews describe the extension as it was when people reviewed it. Disabling is better than nothing, but removal takes the same two minutes.'}},

 {date:'Antivirus',crit:0,beat:'When protection switches itself off',
  body:'Windows Defender and the protection built into macOS are solid defaults for most people, and keeping the built-in one is a perfectly good answer.<br><br>What matters more than which one you run is what you do when it misbehaves.',
  spot:{type:'predict',topic:'av',q:'Your antivirus shows “protection is off”. You turn it back on and it disables itself again. Most likely cause?',
    opts:[
     ['A subscription that needs renewing',0],
     ['Malware already on the machine, switching it off',1],
     ['A recent update that broke compatibility',0]],
    fb:'Assume malware until someone qualified says otherwise. Disabling protection is one of the first things malicious software does, precisely so it can keep working unnoticed.<br><br>Expired subscriptions and broken updates do happen, and they announce themselves differently — a licence warning, an error message. Protection that silently refuses to stay on is the one to treat as an incident: disconnect from the network and tell IT.'}},

 {date:'Networks',crit:0,beat:'What a public network can and cannot see',
  body:'The laptop is only as private as the network it is on.<br><br>At DEF CON in 2019, researchers set up an access point called “Free Conference WiFi”. Hundreds of security professionals connected to it. The researchers could see which sites they visited and, in some cases, far more.<br><br>Sites that use HTTPS protect the contents of what you send to them. A VPN adds a second layer and hides which sites you are visiting at all — which is the part public networks can otherwise read.',
  spot:{type:'quiz',topic:'network',q:'You are on hotel WiFi, about to log into your work email. HTTPS is on. Do you still need a VPN?',
    opts:[
     ['No — HTTPS already encrypts everything that matters',0],
     ['Yes — it hides which services you are using, and covers anything not on HTTPS',1],
     ['Only if the hotel network has no password',0],
     ['Only for banking, not for work email',0]],
    fb:'Use it. HTTPS protects the contents of each connection, but the network still sees which services you connect to, and not everything on a laptop speaks HTTPS. A password on the hotel WiFi means nothing — everyone in the building has it.<br><br>If your company provides a VPN, that is the one to use.'}},

 {scene2:1,date:'Your settings',crit:0,beat:'Three things to check on your laptop',
  body:'Mark whichever you mean to do.',
  spot:{type:'checklist',
    items:[
      {topic:'updates',t:'Turn on automatic updates — system and browser',
       how:'This closes the window between a patch being published and it reaching you, without you deciding anything while busy.',
       steps:['Windows: Settings → Windows Update → turn on automatic updates and restart scheduling','macOS: System Settings → General → Software Update → turn on automatic updates','Your browser updates on restart — restart it today if you cannot remember when you last did'],
       itnote:'On a managed work laptop updates may be pushed for you — IT can confirm, and can tell you what the expected delay is.'},
      {topic:'extensions',t:'Remove browser extensions you do not actively use',
       how:'Each one keeps its permissions and keeps updating itself, including after it changes owner.',
       steps:['Chrome: menu → Extensions → Manage extensions. Firefox: menu → Add-ons. Safari: Settings → Extensions','Remove anything you did not deliberately use this month','Check what the ones you keep are allowed to do — “read and change all your data on all sites” is common and worth a second thought'],
       itnote:'Some companies maintain a list of approved extensions — worth asking whether yours does.'},
      {topic:'network',t:'Sort out what you use on public networks',
       how:'Hotel and café networks are shared with everyone in the building, password or not.',
       steps:['Find out whether your company provides a VPN, and how to turn it on','If it does not, prefer your phone’s hotspot over an open network for anything involving work','Turn off automatic joining of open networks on your laptop'],
       itnote:'Avoid free VPN apps — several have been caught selling the browsing data they were meant to protect.'}
    ]}}
];
