#accept a number from user,
#if<10 then add 200 in the number
#if >=10 but < 30 then add 300 in th number
#if it is >= 30  and < 50 then add 400 into the number
#otherwise add 600 in the number and show the o/p
a=int(input("enetr number"))
if a<10:
    a=a+200
elif a<30:
    a=a+300
elif a<50:
    a=a+400
else:
    a=a+600
print(a)
