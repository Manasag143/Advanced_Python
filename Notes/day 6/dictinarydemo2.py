d={"a":10,"b":20,"c":3}
print(d.pop("a"))  #a:10 will be deleted and it will return 10
print(d)
#d.pop("a2") #exception
v=d.pop("a2",-1)
if v==-1:
    print("not found")
else:
    print("key deleted",v)
print(d.popitem())
print(d)
