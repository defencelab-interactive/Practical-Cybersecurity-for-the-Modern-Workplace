const NODES=[
 {date:'Start here',crit:0,beat:'Set the sharing on this one yourself',
  body:'The signed contract has to go to the client’s lawyer. She works at the client, not at your company. She needs to <b>read</b> it, not change it, and only until the deal closes next month.<br><br>Set all three and share it. Everything you need to get it right is in that paragraph.',
  spot:{type:'share',topic:'scope',
    file:'Hartwell-contract-signed.pdf',
    controls:[
     {id:'who',label:'Who can open it',best:2,
      opts:[
       {t:'Anyone with the link',risk:3,
        why:'Not a password — a key. It works for whoever is holding it, and it is forwarded, pasted into chat, and screenshotted without anyone telling you. You will never see the list of who used it.'},
       {t:'Anyone at your company',risk:2,
        why:'She does not work at your company, so this does not reach her at all — and it does reach every one of your colleagues, which was not the intention either.'},
       {t:'Only the people you name',risk:0,
        why:'She signs in as herself. You get a list of who has access, you can see who opened it, and you can remove her when it is done.'}]},
     {id:'what',label:'What they can do',best:0,
      opts:[
       {t:'View only',risk:0,
        why:'What the task asked for. She can read it; the file cannot be altered, and the signed version stays the signed version.'},
       {t:'Can comment',risk:1,
        why:'Reasonable for a draft under negotiation. For a signed contract it is more than was asked, and comments on an executed document confuse the record later.'},
       {t:'Can edit',risk:3,
        why:'On a signed contract this is the one that matters. Edit rights on many services also include the right to re-share it, so you would be handing over the decision you are making right now.'}]},
     {id:'when',label:'How long',best:1,
      opts:[
       {t:'No expiry',risk:2,
        why:'The default nearly everywhere, and the reason old access piles up. Nothing about this file says it should still be reachable next year.'},
       {t:'Until the deal closes',risk:0,
        why:'An expiry does the tidying you were never going to do. If the date slips, extending takes five seconds; if you forget, it closes itself.'},
       {t:'One-time access',risk:1,
        why:'Tighter than needed. Lawyers reread contracts, and she will be back to check a clause — then you are reissuing links, which is where people start using looser settings to save the hassle.'}]}],
    fb:'Named person, view only, with an end date. Not because tighter is always better — because that is what the task actually described, and the task described it in one short paragraph.<br><br>That is the whole method. The sharing settings are not a security ritual; they are a sentence about who needs what, for how long. The trouble starts when nobody writes the sentence and the default answers it instead.'}},

 {date:'2020–2023',crit:1,beat:'A link to one folder that opened the whole account',
  body:'Now the version where somebody got it wrong at scale.<br><br>Microsoft researchers published open-source AI models on GitHub and included a link so people could download them. Reasonable. The link was supposed to point at the folder holding the models.<br><br>It did not. It had been created with access to <b>the entire storage account</b>, and with permission not just to read but to write and delete. Alongside the models sat 38TB of other data: backups of two employees’ machines, containing passwords, keys, and more than 30,000 internal Teams messages.',
  more:{t:'The part that turned a mistake into three years',
    body:'The link was published in July 2020 with an expiry of October 2021 — so it would have closed itself after fifteen months. In October 2021, rather than reissuing it, someone extended the expiry. The new date was <b>October 2051</b>.<br><br>It was found by outside researchers in June 2023 and revoked two days later. Nearly three years, and nothing in between would have surfaced it: a link that works is indistinguishable from a link that works correctly. No alert fires because nothing is going wrong, as far as the system is concerned. Permission is being used exactly as granted.<br><br>Two things to take from it. Scope and permission are decided once, when the link is made, and nobody re-reads them afterwards. And an expiry is the only part of a share that fails <i>safe</i> — which is why extending one to thirty years undoes more than it looks like.'},
  spot:{type:'quiz',topic:'scope',q:'Why did this run for nearly three years without anyone noticing?',
    opts:[
     ['The researchers hid what they had done',0],
     ['A link working correctly and a link working too broadly look identical',1],
     ['Microsoft had no security monitoring',0],
     ['The data was encrypted, so alerts did not fire',0]],
    fb:'They look the same. The link resolved, people downloaded the models, everything behaved. Nothing was failing, so nothing was reported.<br><br>This is why over-sharing is not caught the way a break-in is caught. A break-in leaves a failed login and an alert. Over-sharing leaves a successful download by someone who was, technically, allowed.'}},

 {date:'Folders',crit:0,beat:'What a folder decides on your behalf',
  body:'That was a link someone made deliberately. Most over-sharing is quieter than that, and it happens through folders.<br><br>You rarely share a file. You put it somewhere — the team folder, the project drive, the shared space that already existed. Whatever that place is shared with, your file is now shared with, and the decision was made by someone else, possibly years ago, for a different set of people.',
  spot:{type:'predict',topic:'folders',q:'You need to put a file with salary data somewhere the two people reviewing it can reach. What is the move?',
    opts:[
     ['Make a new folder, share it with those two, put the file there',1],
     ['Put it in the team folder and rename it so it is not obvious',0],
     ['Put it in the team folder and tell people not to open it',0]],
    fb:'A new place with the right people on it. It takes about twenty seconds and it is the only option here where the access list matches who should see it.<br><br>The other two are the common ones, and they share a flaw: both leave the file reachable by everyone the folder reaches, and rely on those people choosing not to look. An obscure filename is not an access control — and it fails worst against the person who is searching for exactly that word.'}},

 {date:'Afterwards',crit:1,beat:'Access outlasts the reason it was granted',
  body:'The last part is time, and it is the one no process covers.<br><br>People change teams, projects end, contractors finish, agencies get replaced. What ends is the reason for the access. The access itself does not end — it has no idea the project is over, and nothing prompts anyone to remove it.<br><br>This is how a folder arrives at a list of forty people that nobody chose. Each addition was correct on the day it was made.',
  spot:{type:'experience',topic:'review',q:'Think of a shared folder you use most. If you opened its access list right now, how many names would surprise you?',
    scale:['None, I know who is on it','One or two','I have genuinely no idea'],
    note:'“I have genuinely no idea” is the honest answer for most shared folders, and it is not carelessness — nothing in the working week ever asks the question.<br><br>Which is why this one is worth doing on a timer rather than on instinct. Once a quarter, open the access list of the two or three places you keep anything sensitive, and read the names. Not an audit — just reading a list. Almost everyone finds at least one person who left, changed role, or was added for something that finished.'}},

 {scene2:1,date:'Your sharing',crit:0,beat:'Three things to do with what you share',
  body:'Mark whichever you mean to do.',
  spot:{type:'checklist',
    items:[
      {topic:'scope',t:'Name people instead of using a link, for anything confidential',
       how:'A named person signs in as themselves, appears on a list, and can be removed. A link is a key that works for whoever ends up holding it.',
       steps:['When you share, choose the option that asks for an email address rather than the one that produces a link','Keep links for things you would not mind a stranger opening','If a link is the only practical option, set an expiry on it'],
       itnote:'Some organisations restrict link sharing centrally. If your options look narrower than this course describes, that is usually why.'},
      {topic:'folders',t:'Check where a sensitive file is going before you put it there',
       how:'The folder decides who can reach your file, and somebody else decided the folder.',
       steps:['Before saving anything sensitive to a shared space, open that space’s sharing settings and read who has access','If the list is wider than the file deserves, make a new folder for it','Watch for “anyone with the link” inherited from the folder — it applies to everything you add'],
       itnote:''},
      {topic:'review',t:'Put one access review in the calendar',
       how:'Access outlasts its reason, and nothing in the working week prompts you to look.',
       steps:['Pick the two or three places where you keep anything sensitive','Set a recurring reminder — quarterly is enough — to open their access lists and read the names','Remove anyone whose reason has ended: left, changed team, finished the project'],
       itnote:'In a managed environment IT may run access reviews already. Worth asking — if they do, yours is a shorter job.'}
    ]}}
];
