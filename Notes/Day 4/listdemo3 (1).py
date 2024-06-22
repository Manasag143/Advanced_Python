lst2=[12,13,14,11,41,12,13,14]
#to delete the values
#pop remove
#to delete the last value
value=lst2.pop()
#to delete the value at particular position
lst2.pop(4)
print("after pop",lst2)

#to delete by value,
#to delete the first occurance of 100 from the list if found
#throws exception if the number not found
lst2.remove(12)
print("after remove",lst2)


#write the code to delete all occurances of value 100
num=12
lst=[1,2,3,12,10,[12,13,14],20,12,12]

lst.remove(12)
print(lst)
while num in lst:
    lst.remove(num)

lst=[1,2,3,[11,22,33],9,10,["aa","bb","cc"]]
for d in lst:
    if isinstance(d,list):
        print("this is list")
    else:
        print("it is other than list")
    









