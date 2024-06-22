##Numpy assignments
##1. Using numpy create a matrix of size 3 by 5. Create another matrix of 5 by 3
##Perform following operations on the matrices
##1. Display shape of both matrix
##2. Find matrix multiplication
##3. Create another matrix of size 3 by 5 using random numbers
##4. And display addition subtraction and member wise multiplication

import numpy as np

l1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
l2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
a = np.array(l1)
b = np.array(l2)
print(a)
print(b)
print("shape of matrix a is: ", a.shape)
print("shape of matrix b is: ", b.shape)
print(a.dot(b))

c = np.random.randint(10, size=(3,5))
print(c)
if a.shape == b.shape:
    print("addition of matrix a and b are: ", a+b)
if c.shape == b.shape:
    print("addition of matrix b and c are: ", c+b)
if a.shape == c.shape:
    print("addition of matrix c and a are: ", a+c)
if a.shape == b.shape:
    print("subtraction of matrix a and b are: ", a-b)
if c.shape == b.shape:
    print("subtraction of matrix b and c are: ", b-c)
if a.shape == c.shape:
    print("subtraction of matrix c and a are: ", c-a)
if a.shape[0] == b.shape[1]:
    print("multiplication of matrix a and b are: ", a.dot(b))
else:
    print("multiplication not possible")
if b.shape[0] == c.shape[1]:
    print("multiplication of matrix b and c are: ", b.dot(c))
else:
    print("multiplication not possible")
if c.shape[0] == a.shape[1]:
    print("multiplication of matrix c and a are: ", c.dot(a))
else:
    print("multiplication not possible")
if b.shape[0] == a.shape[1]:
    print("multiplication of matrix b and a are: ", b.dot(a))
else:
    print("multiplication not possible")
if c.shape[0] == b.shape[1]:
    print("multiplication of matrix c and b are: ", c.dot(b))
else:
    print("multiplication not possible")
if a.shape[0] == c.shape[1]:
    print("multiplication of matrix a and c are: ", a.dot(c))
else:
    print("multiplication not possible")






