a=11
b=9
print("a",bin(a))
print("b",bin(b))
d=b<<4   #010010000
result=d|a
print(result,"--->",bin(result))
#to separate them
print("mask",int(0b01111))
a1=result&15
print(a1)
b1=result>>4
print(b1)
