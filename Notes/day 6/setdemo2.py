s={12,1,3,"aa"}
s.add("xxxx")
print(s)
s.add(10)
print(s)
#s.add([12,13])  #error
s.update([12,13,10,7,8])
print(s)
print(s.pop())
print(s)
s.remove(10)
print(s)
#s.remove(10)  #error
s.discard(7)
print(s)
