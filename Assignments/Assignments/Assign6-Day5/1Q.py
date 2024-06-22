#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
def check(n1,n2):
    for i in n1:
        if i in n2:
            return True
    return False

n1 = str(input("enter a 1 list\n"))
n2 = str(input("enter a 2 list\n"))
n1 = list(n1.split(" "))
n2 = list(n2.split(" "))
print(check(n1,n2))
 
