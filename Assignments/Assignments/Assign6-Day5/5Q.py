"""In English, present participle is formed by adding suffix -ing to infinite
form: go -> going. A simple set of heuristic rules can be givenas follows:
1. If the verb ends in e, drop the e and add ing (if not exception: be, see,
flee, knee, etc.)
2. If the verb ends in ie, change ie to y and add ing
3. For words consisting of consonant-vowel-consonant, double the final letter
before adding ing .
4. By default just add ing
Your task in this exercise is to define a function make_ing_form()
which given a verb in infinitive form returns its present participle form.
Test your function with words such as lie, see, move and hug."""

def make_ing_form(s):
    if (s[-2]+s[-1]) == "ie":       
           s=s.replace("ie","ying")
    elif s[-1]== "e":
        if s in ["be" ,"see" ,"flee", "knee"]:
            s=s+"ing"
        else:    
            s=s[:-1]+"ing"    
    elif ((s[-3] and s[-1]) not in "aeiou") and (s[-2] in "aeiou"):
           s+=s[-1]+"ing"
    else:
        s=s+"ing"
    return s    
s= input("Enter your word:")
print(make_ing_form(s))
            

