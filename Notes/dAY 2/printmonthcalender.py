#accept number of days in a month, 29,28,30,31
#when the month starts (mon-0,tue-1)
while True:
    numdays=int(input("enter days"))
    if numdays>=28 and numdays<=31:
        break
while True:
    startday=int(input("enetr start day 0-mon 1-tuesday .....6-sunday"))
    if startday>=0 and startday<=6:
        break
print("Mon\tTue\tWed\tThu\tFri\tsat\tsun")
#it will print spaces before 1, useful only for line 1
print("   \t"*startday,end="")
count=startday
for i in range(1,numdays+1):
    print(" "+str(i),end="\t")
    count=count+1
    #to bring the cursor on the next line
    if count==7:
        print()
        count=0
