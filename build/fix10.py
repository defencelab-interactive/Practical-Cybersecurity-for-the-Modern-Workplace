import io
p='courses/10-ai-tools.html'
s=io.open(p,encoding='utf-8').read()
reps=[
# ---- node 3: headings + verifiable body ----
("{date:'The ones already on',crit:0,beat:'The AI features you did not switch on',",
 "{date:'Meeting bots',crit:0,beat:'What a note-taker in your meeting can capture',"),
("body:'That covers what you type. The harder part is what you never typed at all.<br><br>AI is now switched on inside tools you already use — note-takers that join meetings, assistants that summarise your inbox, features that read a document to answer a question about it. Most were enabled by an update, not by you.<br><br>A note-taker is the clearest case. It records the meeting. It usually keeps recording through the part after “thanks everyone”, when two people stay on and talk about something else entirely. Then it emails the transcript to everyone who was invited.',",
 "body:'That covers what you type. The other half is what you never typed at all.<br><br>AI features now ship inside tools people already use — note-takers that join calls, assistants that summarise an inbox, a button that answers questions about the document you have open. Whether yours arrived switched on or was turned on deliberately is worth knowing rather than assuming.<br><br>A meeting note-taker is the clearest case, because three things about it are settled by someone other than you: whether it joins, when it stops, and who gets the transcript afterwards. And a recording runs for as long as the meeting runs — so if nobody ends the meeting, it is still going while the last two people stay on to talk about something else.',"),
("note:'“None that I know of” is the answer worth sitting with, because note-takers are often added by whoever set up the invite rather than by the host, and they appear in the participant list rather than announcing themselves.<br><br>Two habits cover most of it. Look at the participant list before the conversation gets sensitive — the bot is usually sitting in it under a name like <i>Notetaker</i>. And when a meeting ends, end it, rather than letting it run while the last two people talk.'",
 "note:'“None that I know of” is the answer worth checking rather than trusting. A bot joins as a participant, so the participant list is where it shows — and depending on the tool it can be added by whoever created the invite, which means nobody in the room necessarily chose it.<br><br>Two habits work whichever tool you have. Look at the participant list before a conversation turns sensitive. And end meetings properly, rather than leaving one open while the last two people keep talking.<br><br>Then find out once, for your own setup: who is allowed to add a note-taker, whether it announces itself, and where the transcript goes when the call is over. Those three answers differ by tool and by how your organisation configured it, so they are worth looking up rather than guessing.'"),
# ---- headings elsewhere ----
("{date:'When it reads for you',crit:1,beat:'Text the AI reads can give it instructions',",
 "{date:'Summaries',crit:1,beat:'Text the AI reads can act on it like an instruction',"),
("{date:'What comes back',crit:1,beat:'The output arrives with your name on it',",
 "{date:'The output',crit:1,beat:'What it writes goes out with your name on it',"),
# ---- checklist steps ----
("{topic:'ambient',t:'Check the participant list before the real conversation starts',\n       how:'A note-taker records everything after the meeting “ends”, and then sends it to everyone.',\n       steps:['Look at who is in the meeting, including anything that is not a person','If one is recording and the next part should not be, say so — people stop it without argument','End meetings properly rather than letting them run on'],",
 "{topic:'ambient',t:'Find out what your meeting note-taker actually does',\n       how:'Three things are set by someone other than you: who can add it, whether it announces itself, and where the transcript goes.',\n       steps:['Look up those three answers once for the tool your team uses','Check the participant list before a conversation turns sensitive — a bot joins as a participant','End meetings properly rather than leaving one running while the last two people talk'],"),
# ---- sources note ----
("The note-taker and meeting examples describe how these features work; they are not drawn from a reported incident.",
 "The meeting-bot node makes no claim about what any particular tool does by default — who may add a note-taker, when it stops and where the transcript goes differ by tool and by configuration, which is why the action is to look those three up rather than to learn a rule. Nothing in that node is drawn from a reported incident."),
]
for a,b in reps:
    print(('ok  ' if a in s else 'MISS'),b[:62]); s=s.replace(a,b,1)
io.open(p,'w',encoding='utf-8').write(s)
