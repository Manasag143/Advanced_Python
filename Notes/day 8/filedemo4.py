with open("mytext.txt") as fh:
    lst=fh.readlines()
    print(lst)

with open("mytext.txt") as fh:
    s=fh.read()


with open("mytext.txt") as fh:
    s=fh.read(7)
    print(s)
    print(fh.tell())
    #modify the point position 3 characters ahead from current position
    fh.seek(fh.tell()+3)
    print(fh.tell())

