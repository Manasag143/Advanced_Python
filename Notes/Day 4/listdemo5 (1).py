lst=[1,2,3,4]
lst1=lst
lst.append(100)
print(lst,lst1)
lst2=lst.copy()
lst.append(200)
print(lst,lst1,lst2)

lst=[1,2,["a","b","c"],3,4]
lst1=lst.copy()
lst.append(400)
print(lst,lst1)
lst[2].append("d")
print(lst,lst1)

import copy
lst3=copy.deepcopy(lst)
lst[2].append("xxxx")
print(lst,lst3)
