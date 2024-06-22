##Generate a list of lists (NOTE: List should get generated dynamically)
##Accept a number from user and check last digit of the number.
##If it is 1 then add it in the list at 1st position.
##If 0 then it should get added at list in 0th position.
##e.g list should look as follows
##[[10],[51],[52]]
##[[10,30,20,40],[11,31,41,31],[22,32,42]....]
##if user enters 15 then the resultant list should be
##[[10,30,20,40],[11,32,41,31],[22,32,42],[],[],[15]]

l=[]

while True:

    num=int(input("Enter a number:"))
    n=num%10
    if n > len(l):      
         for i in range(0,n+1):
                l.append(list())
            
    l[n].append(num)
    print(l)
    s = int(input("if u want quit then press 0 otherwise 1"))
    if s == 0:
        break

