#tuples are used to return multiple values from a function
#tuples can be used to pass variable number of parametrs to a function

def addition(x,y):
    x=x+10
    y=y+20
    print("in function ",x,y)
    return x+y,x,y

x=10
y=20
s,a,b=addition(x,y)
print(addition(x,y))
print(s,a,b)

def function1(a,b=23,*t):
    print(a,b)
    print(t)

function1(12,13)
function1(1,2,3,4,5,6,7,"a","b")

def findsum(a=23,b=10,*t):
    s=a+b
    for num in t:
        s=s+num
    return s


s=findsum(1,2,3,4,10,23,12,12)
print(f"sum : {s}")
    






