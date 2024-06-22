lst=[10,20,30,5]
#to get the position from the list use enumerate
for indx,d in enumerate(lst): #[(0,10),(1,20)
    print(f"{indx}) {d}")

lst=["Pune","Mumbai","Delhi"]
for num,d in enumerate(lst,100): #[(100,Pune),(101,Mumbai),(102,Delhi)
    print(f"{num}) {d}")


lst=[10,20,30,40,50]
lst1=["Pune","mumbai","Delhi","banglore"]

#zip is used to read multiple lists paralelly
for n,n1 in zip(lst,lst1): #[(10,"Pune"),(20,"mumbai")....]
    print(f"{n}--->{n1}")
