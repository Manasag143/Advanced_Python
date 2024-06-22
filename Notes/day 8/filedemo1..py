import os
fh=None
fh1=None
try:
    fh=open("mytext.txt")
    #to check file exists or not
    if os.path.exists("mycopy.txt"):
        print("file exists")
        fh1=open("mycopy.txt","a")
    else:
        print("file does not exists")
        #open file in write mode, if file is not there it will create
       
        fh1=open("mycopy.txt","w")
    for ln in fh:
        print(ln)
        fh1.write(ln)
except FileNotFoundError as e:
    print("file not found",e)
finally:
    if fh!=None:
        fh.close()
    if fh1!=None:
        fh1.close()
    
