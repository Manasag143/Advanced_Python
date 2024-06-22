s="this is cat, cat is cute, where is you cat?"
pos=s.find("cat") #8
print("find position",pos)
pos1=s.index("cat") #8
print("index position",pos1)
pos=s.find("dog")#-1
print("find position dog",pos)
#pos1=s.index("dog")  #exception
#print("index position dog",pos1)
a=5
for j in range(5):
    a=a+2
    if a<7:
         print("smaller",a)
         break
else:
    print("bigger",a)
