import re
#it helps to create regexp object to store regular expression and flags
#in it

myreg=re.compile("s.*?e",re.I)
s="something is there somewhere"
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

news=re.sub("s.*?e","any",s,count=2,flags=re.I|re.M)
print(news)

news=myreg.sub("any",s,count=2)
print(news)
