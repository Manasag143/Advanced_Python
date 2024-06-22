#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n
s = input("enter a string: ")
n = int(input("Enter minimum length u want "))
a = s.split(" ")
for i in a:
    if len(i) >= n:
            print(i)
