import pandas
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
dict_key = data.keys()


def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        check = input("Do u mean " + w.title() + "?(y/n)")
        if check == "y":
            return data[w.title()]
        elif check == "n":
            return "word does not exit"
        else:
            return "don't understand instruction"
    elif w.upper() in data:
        return data[w.upper()]
    else:
        guess = get_close_matches(w, dict_key, cutoff=0.8)
        if len(guess) > 0:
            check = input("Do u mean " + guess[0] + "?(y/n)" + ": ")
            if check.lower() == "y":
                return data[guess[0]]
            elif check.lower() == "n":
                return "word does not exist!"
            else:
                return "don't understand instruction"
        else:
            return "word does not exist!"


word = input("enter a word: ")

output = translate(word.lower())

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



