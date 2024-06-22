lst=[10,20,30,[12,1,10,23],10,10,3,4,10]
#find the position of 20
print("position of 20:",lst.index(20))
#to find number of occurances of the given value
print("number of occurence of 10",lst.count(10))
lst.reverse()
print("after reverse",lst)
lst=[12,13,14,1,2,5,3,24,72]
#in the list if all the values are of same type then
#only sort is possible, it will sort in ascending order
lst.sort()
print("after sort",lst)
#only sort is possible, it will sort in descending order
lst.sort(reverse=True)
print("after reverse",lst)
#to remove all the elements from the list
#lst.clear()


