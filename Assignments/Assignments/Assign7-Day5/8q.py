##Create a list to store strings in a list in following manner list
##[dxz,axz,bat,rat,cat,pat,bbc,bbm,cbm,....] pat axz
##All list with same character at second position should be consecutive.
##If user adds sat, then the resultant list will be:
##[bat,rat,cat,sat,bbc,bbm,cbm,....]
##If user adds pick, then it should be added at
##[bat,rat,cat,bbc,bbm,cbm,pick]


l = ["dxz","axz","bat","rat","cat","pat","bbc","bbm","cbm"]
print(l)
def create_lst(s):
    for i,j in enumerate(l):
        if l[i][1]== s[1]:
            l.insert(i+1, s)
            return l
    
    l.append(s)
    return l
s = input("Enter Word")
create_lst(s)        
print(l)        
    
