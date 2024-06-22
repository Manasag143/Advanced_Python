# Write a version of a palindrome recognizer that also accepts phrase palindromes such as
''''"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a
potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed
under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!"''''.
#Note that punctuation, capitalization, and spacing are usually ignored.

def is_palindrome(s):
  if s == s[::-1]:
    print("This is Palindrome")
  else:
    print("This is not Palindrome")
def remove(s):
    s=s.replace(" ","")
    s=s.replace("!","")
    s=s.replace("?","")
    s=s.replace(",","")
    s=s.replace(".","")
    s=s.replace("'","")
    s=s.lower()
    return s
s=input("Enter the phrase:")
s=remove(s)
is_palindrome(s)
