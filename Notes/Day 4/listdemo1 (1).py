lst=[] #empty list
lst=[10,20,30,1,2,3]
print("length",len(lst))
#to retrieve the value at given index position
print(lst[3])
lst1=[1,2,3,"xxxx"]
lst2=[12,13,"xxx",[100,200,300]]
#to get the value 200
print("to get the value from nested list:",lst2[3][1])
#to overwrite the value in the list
lst2[1]=100
print(lst2)

#add a value at the end
lst2.append("sssss")
lst2.append(23)
lst2.append([12,11,11])
print(lst2)

#to add multiple values in the list at the end
lst2.extend("abcd")
lst2.extend([11,12,13,22,34])
print(lst2)

# to add in between by position
lst2.insert(1,1000)
print(lst2)

