import re
s="Something is there somewhere"
m=re.search("s.*e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    
m=re.search("s.*?e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

m=re.search("t.*?e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

#match always checks the pattern at the begining of the line
m=re.match("t.*?e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    
