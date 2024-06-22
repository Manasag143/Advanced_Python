##Accept name and new salary for a employee, modify salary of the employee.
##display appropriate message if salary modified. or if name not found.
##note : the new salary should be > current salary otherwise show message wrong salary.
##sampleDict = {
##'emp1': {'name': 'Jhon', 'salary': 7500},
##'emp2': {'name': 'Emma', 'salary': 8000},
##'emp3': {'name': 'Brad', 'salary': 6500}
##}

sampleDict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}

name=input("Enter name to modify")
flag = False
for i,j in enumerate(sampleDict):
    if sampleDict[j]["name"] == name:
        salary=int(input("Enter salary"))
        if salary > sampleDict[j]["salary"]:
            sampleDict[j]["salary"] = salary
            flag = True
            break
        else:
            print("wrong salary")
            flag = True
            break
if flag == False:
    print("Name not found")
print(sampleDict)            
