d={"python":200,"perl":210,"linux":100}
v=d.get("python")
if v!=None:
    print("it exists")
else:
    print("key not exists")

#get with default value
v=d.get("python",-1)
if v!=-1:
    print("it exists")
else:
    print("key does not exists")

v=d.setdefault("perl",150)
print(v)
v=d.setdefault("os",150)
print(v)
print(d)
lst=[100,200,300]
d1=dict.fromkeys(lst,"test")
print(d1)
d2=dict.fromkeys(lst,[1,2,3])
print(d2)
d3={"a":12,"b":13}
d4=d3
d3['c']=100
print(d3,d4)
d5=d3.copy()
d4.clear()










