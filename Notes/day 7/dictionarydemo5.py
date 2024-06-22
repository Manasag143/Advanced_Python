d={"python":200,"perl":250,"OS":300,"Linux":100}
#find number of pages in python book
if 'python' in d:
    print(d['python'])
else:
    print("not found")

#find how many books pages are >210
lst=[]
for k in d.keys(): #[python,perl,os,linux]
    if d[k]>200:
        lst.append((k,d[k]))

if len(lst)>0:
    print(lst)
else:
    print("not found")
lst=[]
for k,v in d.items():
    if v>200:
       lst.append((k,v))

if len(lst)>0:
    print(lst)
else:
    print("not found")




    
    
