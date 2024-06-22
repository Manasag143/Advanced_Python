##4. Create two lists to store cities and locations by accepting values from user.
##Display 1st city and 1st location
##then 2nd city and 2nd location ....... (zip function)
m=int(input("Enter how many city you want?"))
n=int(input("Enter how many locations you want?"))
lst1 = []
lst2 = []

for i in range(0,m):
    lst1.append(input(f"Enter city {i+1} "))
    
for j in range(0,n):      
    lst2.append(input(f"Enter location {j+1} "))

for i,j in zip(lst1,lst2):
     print(i,j)

