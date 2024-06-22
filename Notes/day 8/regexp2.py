#to find all occurences of the given pattern
s="Somethis is there somewhere"
import re
#it returns a list of strings, where the portions of the string
#where pattern matches

lst=re.findall("s.*?e",s,re.I)
if lst!=None:
    print(lst)
else:
    print("not found")


lst=re.finditer("s.*?e",s,re.I)
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.span())
else:
    print("not found")
    
