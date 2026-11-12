import io
def sub(path,reps):
    s=io.open(path,encoding='utf-8').read()
    for a,b in reps:
        print(('  ok  ' if a in s else '  MISS'),path.split('/')[-1],'|',b[:60]); s=s.replace(a,b,1)
    io.open(path,'w',encoding='utf-8').write(s)

sub('courses/07-laptop-security.html',[
# hotel wifi / VPN
("['Yes \\u2014 it hides which services you are using, and covers anything not on HTTPS',1],",
 "['Yes \\u2014 it also hides which services you are using',1],"),
("['Only if the hotel network has no password',0],","['Only if the hotel network has no password on it',0],"),
("['Only for banking, not for work email',0]],","['Only for banking, not for everyday work email',0]],"),
# antivirus
("['Malware already on the machine, switching it off',1],","['Malware on the machine, switching it off',1],"),
("['A subscription that needs renewing',0],","['A subscription that has quietly lapsed',0],"),
])

sub('courses/12-file-sharing.html',[
("['A link working correctly and a link working too broadly look identical',1],",
 "['A working link and a too-broad link look the same',1],"),
("['The researchers hid what they had done',0],","['The researchers concealed what they had done',0],"),
("['Microsoft had no security monitoring',0],","['Microsoft had no monitoring on that account',0],"),
])

sub('courses/09-online-presence.html',[
("['The consulting firm name, and the boss being away',1],","['The firm name, plus the boss being away',1],"),
("['The team\\u2019s faces in the photo',0],","['The team\\u2019s faces and names in the photo',0],"),
("['The three weeks of intense work',0],","['The three weeks of overtime mentioned',0],"),
("['The number of likes the post got',0]],","['The number of likes and comments it got',0]],"),
])

sub('courses/02-social-engineering.html',[
("['Ask them to badge in, and offer to hold the parcels',1]","['Offer to hold the parcels while they badge in',1]"),
("['Let them in, then mention it to reception',0],","['Let them in, then mention it to reception after',0],"),
])

sub('courses/11-data-classification.html',[
("['How much harm would follow if the wrong people had it',1],","['How much harm if the wrong people had it',1],"),
("['A new file containing only the summary, pasted in as values',1],","['A new file with only the summary, pasted as values',1],"),
])

sub('courses/04-passwords-mfa.html',[
("['Badly \\u2014 it is a dictionary word with predictable decorations',1],","['Badly \\u2014 a dictionary word with predictable extras',1],"),
])
