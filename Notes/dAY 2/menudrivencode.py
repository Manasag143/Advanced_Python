import sys
#calculate factorial of a number
def factorial(num):
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    return fact

#to check whether given number is prime or not
def checkprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

#display the table of the given number"
def printtable(num):
    for i in range(1,11):
        print(f"{num} * {i}= {num*i}")


choice=0
while choice!=4:
    choice=int(input("""
    1. factorial
    2. prime number
    3. Table of a number
    4. exit
    choice:"""))
    match choice:
        case 1:
            print("factorial selected")
            num=int(input("enetr number"))
            answer=factorial(num)
            print("Factorial :",answer)
        case 2:
            print("prime number selected")
            num=int(input("enetr number"))
            answer=checkprime(num)
            print("The number is prime" if answer else "The number is not prime")
        case 3:
            print("print table selectd")
            num=int(input("enetr number"))
            printtable(num)
        case 4:
            #sys.exit(0)
            print("Thank you for visiting.....")
        case others:
            print("it is default case")



