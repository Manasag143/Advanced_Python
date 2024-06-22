a=12,13,13,"xxx"   #packing of tuple
a1=(1,2,3,4)     #packing of tuple
'''
x=a[0]
y=a[1]
z=a[2]
p=a[3]
'''
x,y,z,p=a        #unpacking of the tuple
print(x,y,z,p)

a=12
b=20
b,a=a,b

a2=12, #it will create a tuple of length 1
a3=(12,)
a4=tuple()
print(type(a2))


