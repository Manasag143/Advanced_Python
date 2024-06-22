import os
import re
if os.path.exists("mytext.txt"):
    with open("mytext.txt") as fh:
        for ln in fh:
            m=re.search("\d$",ln)
            if m!=None:
                print(ln)
            else:
                print(ln+" pattern not found")
                  
