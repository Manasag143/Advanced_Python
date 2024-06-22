lst2=[1,2,"aaa",[12,13,14],100,200]
# to add in a nested list
lst2[3].append(100)
print(lst2)
lst2[3].extend([1,2,3,4])
print(lst2)
lst2[3].insert(2,1000)

