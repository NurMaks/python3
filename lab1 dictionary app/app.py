import json
from difflib import SequenceMatcher

word = ""
while word != "exit":
    word = input("Enter Word: ")
    data = []
    with open("data.json", "r") as file:
        data = json.load(file)
    try:
        for text in data[word]:
            print(text, " ")
    except:
        for key in data:
            if SequenceMatcher(None, key, word).ratio() > 0.8:
                print("Did you mean ",key," instead?")
                comm = input("Enter Y is yes or N if no: ")
                if comm == "Y":
                    for text in data[key]:
                        print(text, " ")
        print("The word doesn't exist. Please double check it!")
