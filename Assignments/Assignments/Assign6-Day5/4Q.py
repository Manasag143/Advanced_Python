"""Define a simple "spelling correction" function correct() that
takes a string andsees to it that
1) two or more occurrences of the space character is compressed
into one, and
2) inserts an extra space after a period if the period is directly
followed by a letter.
e.g. correct("This is very funny and cool.Indeed!")
should return "This is very funny and cool. Indeed!"""

def correct(s):
    s=s.split()
    s=" ".join(s)
    s=s.replace(".",". ")
    return s    
s=input("Enter your sentence:")
print(correct(s))
