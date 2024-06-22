#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
s = input("enter a string: ")
a = s.split(" ")
L=0
for i in a:
    if len(i) > L:
            L = len(i)
print(f"The longest word of string '{s}' is of length is :",L)
