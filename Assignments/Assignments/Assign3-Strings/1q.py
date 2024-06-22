# 1. Write a program that asks the user how many days are in a month, and what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month.

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
