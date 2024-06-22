'''
import module1
print("in usemodule1")
module1.f1(34)
module1.f2()
'''
'''
#using alias name
import module1 as m1
m1.f1(34)
m1.f2()
'''
#using from (pycache module)
#from module1 import *
#importing module from packages
import myPackages.module2 as m2
m2.f1(10)
m2.f2()
