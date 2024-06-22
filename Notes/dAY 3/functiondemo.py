def f1(a,b,c):
    print(a,b,c)

f1(1,2,3)

def f2(a,b=20,c=30):
    print(a,b,c)
    
f2(10)
f2(12,25)
f2(12,13,14)
f2(b=12,c=13,a=14)

'''
def f3(a=10,b,c=30):
    print(a,b,c)
f3(1,2,3)
'''
