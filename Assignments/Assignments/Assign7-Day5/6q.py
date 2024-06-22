##Write a menu driven program to practice Set functions.
##Write a program to accept names from users and store it in a set.
##Display the following menu:
##print("""1. delete element if exists otherwise
##do not show any errr""")
##print("2. add a elemet")
##print("3. create one more set")
##print("4. union of 2 sets")
##print("4. intersection of 2 sets")
##print("5. difference of 2 sets")
##print("6. convert set into frozenset")
##print("6. exit")

def create_set():
    n = int(input("how many elements you want to enter in set "))
    s=set()
    for i in range(0,n):
        value=input("enter element you want to add ")
        s.add(value)
    return s

choice = 0   

while choice!=8:
    choice=int(input("""1. delete element if exists otherwise do not show any errr
2. add a elemet
3. create one more set
4. union of 2 sets
5. intersection of 2 sets
6. difference of 2 sets
7. convert set into frozenset
8. exit
"""))
    match choice:
        case 1:
            value=input("enter value u want to delete ")
            if value in s:
                  s.remove(value)
            print(s)
        case 2:
            value=input("enter element you want to add ")
            s.add(value)
            print(s)
        case 3:
            s2 = create_set()
            print(s2)
        case 4:
            print("For Set1")
            s1 = create_set()
            print("For Set2")
            s2 = create_set()
            print(f"Union of {s1} and {s2} is ",s1|s2)
        case 5:
            print("For Set1")
            s1 = create_set()
            print("For Set2")
            s2 = create_set()
            print(f"Intersection of {s1} and {s2} is ",s1&s2)
        case 6:
            print("For Set1")
            s1 = create_set()
            print("For Set2")
            s2 = create_set()
            print(f"Difference of {s1} and {s2} is  ",s1-s2)
            print(f"Difference of {s2} and {s1} is \n",s2-s1)
        case 7:
            print("create set")
            s = create_set()
            print("convert set into frozenset")
            s = frozenset(s)
            print(s)

        case 8:
            print("Thank You for visiting!")
            
            
          
          
          
          
