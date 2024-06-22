"""Write a recursive sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:

1, if x = 1
x + sum from 1 to x-1 if x > 1
Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
+ 10
def sum(x):
# you complete this function recursively
def main():
# compute and print 1 + 2 + ... + 10
print(sum(10))
main()
"""

def sum(x):
  if x == 1:
    return 1
  return x + sum(x-1)
n=int(input("enter a number :"))  
print(f"Sum of starting {n} numbers is ",sum(n))
