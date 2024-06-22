course={"DAI":(60,300),"DUASP":(40,350),"DAC":(240,400)}
def addnewcourse():
    cname=input("enetr course name")
    capacity=int(input("enetr capacity"))
    duration=int(input("enter duration"))
    v=course.get(cname,-1)
    #if key is not there add it
    if v==-1:
        course[cname]=capacity,duration
        return True
    else:
        return False
    
#delete by name
def deletebyname(cname):
    if cname in course:
        ans=input(f"{cname}, {course[cname]} do you want to delete(y/n)?")
        if ans=="y":
            course.pop(cname)
            return 1
        else:
            return 2
    else:
        return 3
                  
#to update details of a course
def updatecourse(cname,capacity,duration):
    if cname in course:
        ans=input(f"{cname}, {course[cname]} do you want to update(y/n)?")
        if ans=="y":
            course[cname]=capacity,duration
            return 1
        else:
            return 2
    else:
        return 3

#find all courses with capacity >= given capacity
def findByCapacity(c):
    lst=[]
    for k,v in course.items():
        if v[0]>=c:
            lst.append((k,v))
    if len(lst)>0:
        return lst
    else:
        return None
     
def displaybycname(cname):
    if cname in course:
        return course[cname]
    else:
        return None
#display all the values from the given dictionary
def displayall():
    for k,v in course.items():
        print(f"{k}---->{v}")

#display data in sorted order of keys
def displayinsortedorder():
    for k in sorted(course.keys()):
        print(f"{k} ---> {course[k]}")
        
choice=0
while choice!=9:
    choice=int(input("""1. add new course
2. delete course
3. update course
4. dispaly all
5. display by capacity
6. display in sorted order by name
7. display by cname
8. display by duration
9. exit
chice: """))
    match choice:
        case 1:
            addnewcourse()
        case 2:
            cname=input("enetr coursename to delete")
            status=deletebyname(cname)
            if status==1:
                print("found and deleted")
            elif status==2:
                print("found and not deleted")
            else:
                print("not found")
        case 3:
            cname=input("enter coursename to modify")
            capacity=int(input("enetr capacity"))
            duration=int(input("enetr duration"))
            status=updatecourse(cname,capacity,duration)
            if status==1:
                print("found and updated")
            elif status==2:
                print("found and not updates")
            else:
                print("not found")
        case 4:
            displayall()
        case 5:
            c=int(input("enter capacity to search"))
            lst=findByCapacity(c)
            if lst!=None:
                for data in lst:
                    print(f"{data}")
            else:
                print("not found")
                
        case 6:
            displayinsortedorder()
        case 7:
            cname=input("enetr course name")
            c=displaybycname(cname)
            if c!=None:
                print(f"{cname}--->{c}")
            else:
                print("not found")
        case 8:
            pass
        case 9:
            print("Thank you for visiting...")
        case _:
            print("wrong choice")
            pass
