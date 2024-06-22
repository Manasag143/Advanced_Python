a=10
b=10
c=a
print(id(a),id(b),id(c))
print(a is b)
a=15
print(id(a),id(b),id(c))
d=int(input("enetr number"))
print(d,id(d))
s1="Rajan"
s2=s1
s3="Rajan"
print(id(s1),id(s2),id(s3))
print("Rajan" is s2)
s1="Revati"
print(id(s1),id(s2),id(s3))
s4=input("enter name")
print(s4,id(s4))
