import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    #w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
      #  return "did you mean %s instant ? "%get_close_matches(w,data.keys())[0]
        y=input("did you mean %s instant ? "%get_close_matches(w,data.keys())[0])
        if y =="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif y=="n":
            return "Thank You...Have a Nice Day....."
    else:
        return "data not found..."
word=input("Search :")
print(translate(word))
output=translate(word)
if type(word)==list:
    for item in output:
        print(item)
else:
        print(output)
