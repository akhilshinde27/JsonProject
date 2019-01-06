import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))
print(SequenceMatcher(None,"rainn","rain").ratio())
print(get_close_matches("access road",data.keys(),n=2))
print(data.keys())
print(type(data.keys()))
