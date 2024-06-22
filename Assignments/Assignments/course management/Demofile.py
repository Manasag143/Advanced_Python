import os
import re

with open("mytext.txt") as fh:
       lst=fh.readlines()
       print(lst)

with open("mytext.txt") as fh:
       s=fh.read(10)
       print(s)
       print(fh.tell())
       fh.seek(fh.tell()+3)
       print(fh.tell())
       
