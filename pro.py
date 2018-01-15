import json,time
from difflib import get_close_matches

data= json.load(open("data.json"))

def get(strn):   # create the same func with exception handling
    if strn in data:
        return(data[strn])
    elif strn.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[strn.title()]
    elif strn.upper() in data: #in case user enters words like USA or NATO
        return data[strn.upper()]
    elif len(get_close_matches(strn , data.keys() )) > 0:
        feed=input("Do you mean %s instead? Enter Y if Yes or N if No: \n" % get_close_matches(strn, data.keys())[0])
        if feed=="y":        #add "Y"and "YES.lower()"
            return data[get_close_matches(strn, data.keys())[0]]
        elif feed=="n":
            return "The word doesn't exist"
        else:
            return "Not able to understand your input"
    else:
        return "The word doesn't exist"



strn=input("Enter a word: \n")
word = (get(strn.lower()))
if type(word)==list:  #this removes the brackets from the output
    for i in word:
        print(i)
else:
    print (word)

time.sleep(5)
"""
    try:
        return(data[strn])
    try:

    except:

        return("The word doesn't exist")
"""
"""

  can use if condition given below


        if strn in word:
            return(data[strn])
        else:
            return("The word doesn't exist")


"""
