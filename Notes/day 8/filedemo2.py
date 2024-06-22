with open("mytext.txt") as fh:
    with open("mycopy11.txt","w") as fh1:
        for ln in fh:
            ln=ln.rstrip('\n')
            print(ln)
            fh1.write(ln+"\n")
            
