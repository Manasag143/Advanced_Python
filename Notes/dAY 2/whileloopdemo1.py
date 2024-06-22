#to find addition of digits of the number
num=int(input("enetr number"))
s=0
#345345
while num>0:
    d=num%10
    num=num//10
    s=s+d
print("sum of digits:",s)
