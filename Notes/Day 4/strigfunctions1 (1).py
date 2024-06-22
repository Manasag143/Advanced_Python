s="this is cat, cat is cute, where is you cat?"
pos=s.find('cat')
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
print("*"*60)
pos=s.rfind('cat')
print("position :",pos)
pos=s.rfind('cat')
print("position :",0,pos-1)

#to find position of all occurences of the given string
search=input("enetr string to search")
pos=s.find(search)
while pos!=-1:
    print("position :",pos)
    pos=s.find(search,pos+1)
