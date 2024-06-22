##1. Write a menu driven program to practice String functions
##Design following menu
##a. display characters from even position
##b. display characters from odd position
##c. display length of a string
##d. add a at the end of string length times
##e. exit
def even_pos(s):
    j=1
    for i in s:
        if j%2 == 0:
            print(i,end="")
        j+=1

def odd_pos(s):
    j=1
    for i in s:
        if j%2 != 0:
            print(i,end="")
        j+=1
    
s=input("Enter a string:\n")
choice = 0
while choice!='e':
    choice=input('''
a. display characters from even position
b. display characters from odd position
c. display length of a string
d. add a at the end of string length times
e. exit
''')
    match choice:
        case "a":
            print("Characters from even positions are as follows:")
            even_pos(s)
        case "b":
            print("Characters from odd positions are as follows:")
            odd_pos(s)
        case "c":
            print("Length of the string is:",len(s))
        case "d":
            print("New string is:")
            s+="a"*len(s)
            print(s)
        case "e":
            print("thank you for visiting")
        case _:
            print("Enter correct choice")
            
    
