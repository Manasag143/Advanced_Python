s=set(['python','perl','Perl','linux','python','os'])
print(s)
print("length : ",len(s))
#to retrieve all values from the set use for loop
for s1 in s:
    print(s1)

#to check whether string python exists in the set or not
print('python' in s)

#To convert string into set
s=set("this is string")
print(s)

#to create empty set
s2=set()

s={1,2,3,"xxxx",(23,"m",[10,20],34),23}
print(s)
