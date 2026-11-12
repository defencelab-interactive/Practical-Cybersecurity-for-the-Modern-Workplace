import io
def sub(path,reps):
    s=io.open(path,encoding='utf-8').read()
    for a,b in reps:
        print(('  ok  ' if a in s else '  MISS'),path.split('/')[-1],'|',b[:62]); s=s.replace(a,b,1)
    io.open(path,'w',encoding='utf-8').write(s)

# ---- course 2: "It" names nothing ----
sub('courses/02-social-engineering.html',[
("<title>Defence Lab · How People Get Talked Into It</title>","<title>Defence Lab · The Phone Call, the Door and the USB Stick</title>"),
("<h1>How People Get Talked Into It</h1>","<h1>The Phone Call, the Door and the USB Stick</h1>"),
])

# ---- course 12: "This" names nothing ----
sub('courses/12-file-sharing.html',[
("<title>Defence Lab · Who Else Can Open This</title>","<title>Defence Lab · Share Links, Folders and Old Access</title>"),
("<h1>Who Else Can Open This</h1>","<h1>Share Links, Folders and Old Access</h1>"),
("beat:'Set the sharing on this one yourself'","beat:'Set the sharing on this contract yourself'"),
("{date:'Afterwards',crit:1,beat:'Access outlasts the reason it was granted'","{date:'Months later',crit:1,beat:'Access outlasts the reason it was granted'"),
("more:{t:'The part that turned a mistake into three years'","more:{t:'The expiry that was extended to 2051'"),
])

# ---- course 3: rail label repeated the heading ----
sub('courses/03-physical-security.html',[
("{date:'A news photo',crit:1,beat:'A password published in a news photo'","{date:'Hawaii, 2017',crit:1,beat:'A password published in a news photo'"),
])

# ---- course 4: rail label repeated the heading; vague 'even so' ----
sub('courses/04-passwords-mfa.html',[
("beat:'47 accounts opened in under an hour'","beat:'Every account that shared that password'"),
("beat:'Why the second step matters even so'","beat:'What the second step adds once the password is gone'"),
])

# ---- course 8: trailer-style deep dive ----
sub('courses/08-phone-security.html',[
("more:{t:'The part people only discover afterwards: your authenticator'","more:{t:'Losing the phone means losing your authenticator'"),
])

# ---- landing + catalogue ----
i=io.open('index.html',encoding='utf-8').read()
for a,b in [("'How People Get Talked Into It'","'The Phone Call, the Door and the USB Stick'"),
            ("'Who Else Can Open This'","'Share Links, Folders and Old Access'")]:
    print(('  ok  ' if a in i else '  MISS'),'index |',b); i=i.replace(a,b,1)
io.open('index.html','w',encoding='utf-8').write(i)

c=io.open('CATALOGUE.md',encoding='utf-8').read()
for a,b in [("| 2 | **Social Engineering: How People Get Played**","| 2 | **The Phone Call, the Door and the USB Stick**"),
            ("| 12 | **Who Else Can Open This**","| 12 | **Share Links, Folders and Old Access**"),
            ("| Course 2 | How People Get Talked Into It","| Course 2 | The Phone Call, the Door and the USB Stick"),
            ("| 3 | Course | How People Get Talked Into It","| 3 | Course | The Phone Call, the Door and the USB Stick"),
            ("| 22 | Course | File Sharing & Access","| 22 | Course | Share Links, Folders and Old Access")]:
    print(('  ok  ' if a in c else '  MISS'),'cat |',b[:56]); c=c.replace(a,b,1)
io.open('CATALOGUE.md','w',encoding='utf-8').write(c)
