#scope of variable
def f1():
    #global x
    x=23
    print("in f1",x)
    x=x+10
    print(x)
    def f2():
        #global x
        nonlocal x
        x=55
        print("in f2",x)
    f2()
    print("after f2 call",x)    
        



x=100
print("before f1 call",x)
f1()
print("after f1 call",x)
