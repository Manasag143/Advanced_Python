#A pangram is a sentence that contains all the letters of the English alphabet at least once, for
''''example: The quick brown fox, jumps over the lazy dog!!!!.
Your task here is to write a function to check a sentence to see if it is a pangram or not.''''

import string

def ispangram(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False

	return True

string = input("Enter you sentence:")
if(ispangram(string) == True):
	print("This is Pangram")
else:
	print("This is not Pangram")
