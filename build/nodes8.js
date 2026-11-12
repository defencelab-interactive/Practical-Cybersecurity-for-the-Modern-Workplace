const NODES=[
 {date:'Start here',crit:0,beat:'Which one would hurt more to lose?',
  body:'Both are taken on the same afternoon. Before you pick, read what is actually on each.',
  spot:{type:'weigh',topic:'reach',q:'Stolen on the same day — which costs you more?',
    sides:[
     {ic:'💻',t:'Your work laptop',
      items:['Work files and email','Access to the company network','Saved browser passwords','Documents you were drafting'],
      pick:'The laptop'},
     {ic:'📱',t:'Your phone',
      items:['Work and personal email','Banking apps, already signed in','Your authenticator codes','Messages, photos, location history','The number your bank texts for confirmation'],
      pick:'The phone'}],
    right:1,
    fb:'The phone, and it is not close.<br><br>A laptop holds work. A phone holds the <b>means of getting back into everything else</b> — your authenticator codes, your email for password resets, and the number used to confirm it is really you. Someone holding an unlocked phone can often reset accounts that were never on the phone at all.<br><br>Which is why a phone deserves at least the care people give a laptop, and usually gets less.'}},

 {date:'Permissions',crit:0,beat:'What your apps can see when you are not looking',
  body:'Start with what is already installed. Apps ask for permissions at install and keep them indefinitely — location, microphone, camera, contacts — whether or not they still need them.<br><br>In 2021 a flashlight app with tens of millions of downloads was found requesting contacts, location, camera and microphone. A flashlight needs a torch and nothing else.',
  spot:{type:'quiz',topic:'perms',q:'A weather app you installed a year ago wants your contacts and microphone. What do you do?',
    opts:[
     ['Allow it — weather apps use extra data sources',0],
     ['Allow contacts but deny the microphone',0],
     ['Deny both — weather needs neither',1],
     ['Leave the settings and just stop using the app',0]],
    fb:'Deny both. Weather needs a location, optionally, and an internet connection. Contacts and a microphone have nothing to do with forecasting, and a request for them says the app is collecting beyond its stated purpose.<br><br>Leaving an unused app installed changes nothing — the permissions stay live whether you open it or not.'}},

 {date:'Charging and WiFi',crit:1,beat:'Why that airport USB socket is not just power',
  body:'Permissions are what you granted. These two are what you walk into.<br><br>A USB cable carries power and data on the same connector. A tampered public charging point can read from the phone while it charges — the FBI and FCC both issued warnings about it. A wall socket with your own adapter carries power only.<br><br>Public WiFi has the same shape. At DEF CON in 2019, researchers put up an access point called “Free Conference WiFi” and hundreds of security professionals joined it.',
  spot:{type:'predict',topic:'public',q:'Airport, 5% battery, boarding soon. A free USB charging post, or a wall socket across the hall.',
    opts:[
     ['Use the USB post — you need the charge now',0],
     ['Walk to the wall socket and use your own adapter',1],
     ['Use the USB post, but switch the phone off first',0]],
    fb:'The wall socket. Your own adapter carries power and nothing else, which removes the question entirely.<br><br>Switching the phone off helps on some devices and not others, and “charge only” prompts can be bypassed on tampered hardware. A USB data blocker costs about the price of a coffee and solves it permanently if you travel often.'}},

 {date:'If it goes missing',crit:1,beat:'The order to do things in',
  body:'Assume it happens. What you do in the first ten minutes decides most of the rest.<br><br><b>Lock it remotely</b> first — that stops anything further without destroying evidence of where it is. <b>Then tell IT</b>, if it is a work phone or has work accounts on it. <b>Then change the passwords</b> for anything that was signed in. Wipe it only when you are sure it is gone rather than misplaced, because a wipe is permanent and ends the chance of finding it.<br><br>All of that needs Find My Device switched on beforehand. It cannot be turned on afterwards.',
  more:{t:'The part people only discover afterwards: your authenticator',
    body:'If your second factor lives in an authenticator app and the phone is gone without a backup, you are locked out of every account that uses it — including the email you would normally use to recover the others. People discover this at the worst possible moment.<br><br>Two things prevent it. <b>Cloud backup</b> in the authenticator: Google Authenticator has “Use on multiple devices”, Microsoft Authenticator has cloud backup in its settings, Authy backs up by default. And <b>recovery codes</b> — the one-time codes each service offers when you first switch MFA on. Keep them somewhere physical, not on the phone they would recover.<br><br>Both at once is not paranoid. Cloud backup fails quietly if the account it syncs to is also on the lost phone.'},
  spot:{type:'quiz',topic:'lost',q:'Your phone is stolen from a table. What comes first?',
    opts:[
     ['Wipe it immediately before anyone gets in',0],
     ['Lock it remotely, then notify and change passwords',1],
     ['Change your passwords first, from another device',0],
     ['Report it to the police, then decide',0]],
    fb:'Lock first. It blocks use straight away, keeps location reporting alive, and is reversible if the phone turns up in a coat pocket.<br><br>Wiping first throws away the chance of recovering it and does nothing extra for accounts. Changing passwords matters, but after the device itself is out of reach. Police reports matter for insurance, not for the next ten minutes.'}},

 {scene2:1,date:'Your settings',crit:0,beat:'Three things to check on your phone',
  body:'Mark whichever you mean to do.',
  spot:{type:'checklist',
    items:[
      {topic:'lost',t:'Turn on Find My Device, and check that it works',
       how:'It cannot be enabled after the phone is gone, and an untested setting is a guess.',
       steps:['iPhone: Settings → your name → Find My → turn on all three options','Android: Settings → Google → Find My Device, and confirm Location is on','Test it from a browser — icloud.com/find or android.com/find — and confirm your phone appears'],
       itnote:'A managed work phone may already have remote wipe through IT. Worth knowing whether yours does, and who to call.'},
      {topic:'lost',t:'Back up your authenticator, and keep recovery codes off the phone',
       how:'Losing the phone should not mean losing the way back into everything on it.',
       steps:['Open your authenticator app and turn on cloud backup or multi-device','Find the recovery codes for your two or three most important accounts','Keep them somewhere physical — not in the phone they would be recovering'],
       itnote:''},
      {topic:'perms',t:'Review what your apps are allowed to reach',
       how:'Permissions granted once stay granted, including for apps you no longer open.',
       steps:['iPhone: Settings → Privacy & Security → Location, Camera, Microphone','Android: Settings → Apps → Permission manager','Change “Always” location to “While Using” for everything except Find My Device, and delete apps you have not opened in months'],
       itnote:''}
    ]}}
];
