import re

def sp(password):
    if len(password) >= 8:
        #print("satisfied length condition")
        
        patternd = re.compile(r'''(
            \d{1,}
            
        )''', re.VERBOSE)
        patterna = re.compile(r'''(
           
            [a-z]{1,}  
        )''', re.VERBOSE)
        patternA = re.compile(r'''(
           
            [A-Z]{1,}  
        )''', re.VERBOSE)

        if patternd.search(password) and patterna.search(password)  and patternA.search(password):
            print("satisfied")
        else:
            print("password not satisfied")
    else:
        print("not 8 characters")

def sp1(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8}$')
    if pattern.search(password):
        print("satisfied")
    else:
        print("password not satisfied")


sp1("asdfghA1")