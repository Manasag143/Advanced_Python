#to chek the number is prime or not
num=int(input("enter a number"))
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if flag:
    print("the number is not prime")
else:
    print("the number is prime")

#9
    #5
for i in range(2,num):
    if num%i==0:
        print("The number is not prime")
        break
else: #if break statement does not get executed
    print("The number is prime")

