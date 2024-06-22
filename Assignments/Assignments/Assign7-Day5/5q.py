##Create a list and exchange the values as index and index as values.
##lst=[12, 1, 3, 7, 8, 5, 8]
##0 1 2 3 4 5 6
##
##Output should be as follows.
##lst1=[-1 ,1, -1, 2, -1, 5, -1, 3, 6, -1, -1, -1, 0]

lst=[12, 1, 3, 7, 8, 5, 8]
n = max(lst)
l = [-1] * (n+1)
for i in range(0,len(lst)):
    l[lst[i]] = i
print(l)        
    
