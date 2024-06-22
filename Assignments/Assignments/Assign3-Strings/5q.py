#Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
"""That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon".""""
import string
def ispangram(str):
  a=""
  for i in str:
    if i not in "aeiouAEIOU":
          a = a + i + "o" + i          
    else:
          a = a + i
  return a
	
string = input("Enter you sentence:")
print(ispangram(string))
