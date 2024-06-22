##Write a python program to accept mobile number and validate it. it should contain exactly
##10 digits.
import re

num = int(input("Enter mobile number"))

m=re.search('^\d{10}$',num)
print(m)

