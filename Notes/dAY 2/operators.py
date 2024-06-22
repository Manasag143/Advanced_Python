#to find maximum of 3 numbers
a=int(input("enter number"))  #always accepts and store data in the form of strings
b=int(input("enetr number2"))
c=int(input("enter number 3"))
if a>b and a>c:
    print("a is the maixmum value",a)
else:
    if b>a and b>c:
        print("b is the maixmum value",b)
    else:
        print("c is the maximum value",c)

if a>b and a>c:
    print("a is the maixmum value",a)
elif b>a and b>c:
    print("b is the maixmum value",b)
else:
    print("c is the maximum value",c)
    
print("addition:",a+b,a,b,sep=":")
print("addition : ",end="--->")
print(a+b)
print("welcome")


a=23
b=35
m=a if a>b else b
