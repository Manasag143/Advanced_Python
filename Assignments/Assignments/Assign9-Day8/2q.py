#Accept lines from user and display only the lines that start
#with a number or any 2 alphabets
##    import re
##
##    print("enter lines")
##    lines = []
##    while True:
##        line = input("")
##        if line:
##            lines.append(line)
##        else:
##            break
##    text = '\n'.join(lines)
##
##    print(text)
##
##    m=re.search('^[0-9]',text)
##    if m!= None:
##        print(text)

import re

# Accepts lines from user
lines = []
print("Enter the lines (type 'END' to stop):")
while True:
    line = input()
    if line.upper() == "END":
        break
    lines.append(line)

# Check each line using regular expression
for line in lines:
    # Check if the line starts with a number or any 2 alphabets
    if re.match(r'^\d|[a-zA-Z]{2}', line):
        print(line)
