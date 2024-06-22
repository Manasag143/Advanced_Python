##1. accept numbers from user and store it in a list1 and list2
##then convert these list into ndarray
##create list3 and list4 to store numbers
##and convert it into ndarray
##(list1 and list 2 in one array)
##(list3 and list 4 in another array)
##combine these 4 arrays into 2D arrays (use stack functions)
##
##and find memberwise addition,multiplication
##and exponential of first array
l1=[]
l2=[]

def convert(l):
    n=int(input("Enter how many numbers you want to enter: "))
    for i in range(0,n):
        l.append(int(input("enter a number u want to add in list: ")))
convert(l1)
print(l1)
convert(l2)
print(l2)
          
