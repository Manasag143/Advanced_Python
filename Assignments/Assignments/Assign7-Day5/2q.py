##Write a program to accept a string from user.
##Accept a second string from user to search and find all occurrences of in the given string.
##e.g
##s1=This is string
##check=is
##is-2
##is-5
##count=2
##
##s1=”this is cat and cat is cute, where is your cat?”
##check=cat
##cat-8
##cat-16
##cat-43

s1=input("Enter a string : ")
s2=input("Enter string you want to find : ")
count=0
pos=s1.find(s2)
while pos!=-1:
    print(f" position of {s2}:",pos)
    count+=1
    pos=s1.find(s2,pos+1)
print("count - ",count)
