'''Write a menu driven program to practice List functions.
Validate input data wherever required.
Display following menu:
1. Accept Data
a) add at last position
b) add at given position
2. Delete data by value
display message deleted successfully
or not found
3. delete data by position
a) delete last element
b) delete from particular position
4. sort
a) ascending
b) descending
5. reverse
6. Print in sorted order without changing original list
7. print in reverse order without changing original list
8. display data
a) normal
b) numbered'''
def add_data(l):
    ch=input('''
a add at last position
b add at given position \n''')
    n = int(input("how many data item you want to add:  "))
    if ch == "a":
        for i in range(0,n):
            data = input("enter data item:  ")
            l.append(data)

    elif ch == "b":
            pos = int(input("which position you want to add data"))
            for i in range(pos,n+pos):
                data = input("enter data item")
                l.insert(i,data)
    return l    

def del_value(value):   
    for i in l:
        if i == value:
            a = input(f"are you sure you want to delete {value}?\n yes --> Y \n no --> N\n")
            if a == "Y":
                return 1
            else:
                return 0
    return -1

def del_pos():
     n = input(f""" delete data by position
a) delete last element
b) delete from particular position""")
     if n == "a":
         a = input("are you sure you want to delete last element?\n yes --> Y \n no --> N\n")
         if a == "Y":
                  l.pop()
                  print("last element deleted successfully")
         else:
                  print("last element not deleted")
     else:
        a = input("are you sure you want to delete element?\n yes --> Y \n no --> N\n")
        if a == "Y":
                pos= int(input(f"Enter position u want to delete from:\n {l}"))
                l.pop(pos)
                print("element deleted successfully")
        else:
                print("element not deleted")
     print(l)           
        
l =[]
choice = 0
while choice != 9:
    choice= int(input("""
1. Accept Data
2. Delete data by value
3. delete data by position
4. sort
5. reverse
6. Print in sorted order without changing original list
7. print in reverse order without changing original list
8. display data
9. exit
    """))

    match choice :
                case 1:
                    print(add_data(l))
                case 2:
                    n = input(f"Enter value that you want to delete from the list:\n {l} \n")
                    a = del_value(n)
                    if a == 1:
                        l.remove(n)
                        print(f"value {n} deleted successfully")
                    elif a == -1:
                        print(f"value {n} not found")
                    else:
                        print(f"value {n} not deleted")
                case 3:
                   del_pos()
                case 4:
                    n=input("Sort By a) ascending b) descending")
                    if n=="a":
                        print(l.sort())
                    else:
                        print(l.sort(reverse = True))
                    print("sorted successfully \n ",l)
                case 5:
                    l = l[::-1]
                    print(l)
                case 6:
                    n=input("Sort By a) ascending b) descending")
                    lst=l.copy()
                    if n=="a":
                        lst.sort()
                    else:
                        lst.sort(reverse = True)
                    print("sorted successfully \n ",lst)
                case 7:
                    print(l[::-1])
                case 8:
                    print(l)
                case 9:
                    print("ok")



                





    
