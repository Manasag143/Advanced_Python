"""Write a program that contains a function that has one parameter, n, representing an integer
greater than 0. The function should return n! (n factorial). Then write a main function that calls
this function with the values 1 through 20, one at a time, printing the returned results. This is
what your output should look like:
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 628800
"""

n1=int(input("enter a starting range:"))
n2=int(input("enter a ending range:"))
def fact(a):
  if a==0 or a==1:
    return 1
  return a*fact(a-1)
for i in range(n1,n2+1):
  print(f"factorial of {i} is:",fact(i))
