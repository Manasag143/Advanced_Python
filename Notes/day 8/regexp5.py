import re
s="This is home"
m=re.search("^(\w+)\s(\w+)\s\w+$",s,re.I)
if m!=None:
    print(m.group(1))
    print(m.span(1))
    print(m.group(2))
    print(m.span(2))
    print(m.group())
    print(m.span())
else:
    print("not found")

acno="XXXXX1234XXXXX"
m=re.search("^X{5}(\d{4})X{5}",acno)
if m!=None:
    print(m.group(1))
    print(m.span(1))

