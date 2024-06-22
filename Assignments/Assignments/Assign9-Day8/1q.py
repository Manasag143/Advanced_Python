##write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
##example myemail@google.com o/p myemail
import re
email=input("Enter Email")
m=re.search("(\w.*)@(.*)",email,re.I)
if m != None:
    print(m.group(1))
else:
    print("Incorrect Email")
