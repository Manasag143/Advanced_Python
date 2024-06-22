#numpy is useful for handling n dimenssinal 
#array, arrays are homogeneous

import numpy as np
#create 1D array
a=np.array([12,13,23.78,45])
print(a)
#the type of a
print("array type ",type(a))
#the type of data in the array
print("data type",a.dtype)
print("Dimensions: ",a.ndim) #find dimenssions
#to find number of rows and columns
print("shape :",a.shape)   




a=np.array([["xxx","yyy"],["zzz","pppp"]])
print(a)
print("array type ",type(a))
print("data type",a.dtype)
print("Dimensions: ",a.ndim) #find dimenssions
print("shape :",a.shape)

#create 2d array
import numpy as np
a=np.array([[12,13,23.78,45],[45,22,45,55]])
print(a)
print("array type ",type(a))
print("data type",a.dtype)
print("Dimensions: ",a.ndim) #find dimenssions
print("shape :",a.shape)

#create 3D array

s=np.array([[[1,2,3],[10,20,30]],[[5,6,7],[8,9,10]]])
print(s)
print("array type ",type(s))
print("data type",s.dtype)
print("Dimensions: ",s.ndim) #find dimenssions
print("shape :",s.shape)

#add 0 to 11 in array b
b=np.arange(12)
c=np.arange(1,32,2).reshape(4,4)
print(c)
print(c[1:3,2:4])
print(c[1,-1])


#to arrange data columnwise
c=np.arange(1,32,2).reshape(4,4,order='f')
print(c)

c[2,1]=231

a=np.zeros((3,3),dtype='int32')
b=np.ones((3,3))
c=np.empty((3,3))
print(a)
print(b)
print(c)


#memberwise addition
a=a+b
print(a)
a=a+10
print(a)
#memberwise multiplication
print(a*b)
#matrix multiplication
print(a.dot(b))




#identity matrix
a=np.identity(3)
print(a)
b=np.eye(3,4)
print(b)
b=np.eye(4,5,k=1)
print(b)



#filter the array

a=np.array([[12,13,14,15],[3,24,13,6],[10,18,1,2]])
print(a[a%6==0])
print(a[a>5])

#to search the value
print(np.where(a%2==0))
print(list(np.where(a%2==0)[0].data))

#to find sum of all values
print(np.sum(a,axis=1)) # row wise sum
print(np.sum(a,axis=0)) # column wise sum
print(np.sum(a)) # sum of all values

#to find mean
print(np.mean(a))
print(np.mean(a,axis=1))

#hstack and vstack
x=np.array([10,20,30])
y=np.array([11,12,13])
z=np.array([21,22,23])

#to arrange data horizontally
print(np.hstack((x,y,z)))

d=np.vstack((x,y,z))
print(np.vstack((x,y,z)))


#revesrse columns and rows both
print(np.flip(d))
#flips the rows, the 1st row will be the last row
#last row will be the first row
print(np.flip(d,axis=1)) 

#endpoint=False will exclude 30
x=np.linspace(10,30,7,endpoint=False)
print(x)

student=np.array([[40,50,48],[30,35,38],[44,38,48]])
print(student)

avmks=np.mean(student,axis=1)
print(avmks)
names=['student1','student2','student3']
import matplotlib.pyplot as plt
plt.pie(avmks,labels=names)
plt.bar(names,avmks)







