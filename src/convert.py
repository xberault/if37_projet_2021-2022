import json
import os

test = "Tous les acheteur"

data_file = os.path.join("data", "dico.json")
with open(__file__.replace("convert.py", data_file)) as f:
    data = json.load(f)


def extractWords(text):
    return text.split()

def getMascWords():
    out = []
    for word in data:
        out.append(word['MASC'])
    return out

def convert(splittedText):
    out = splittedText
    d = getMascWords()
    for word in out:
        if word.lower() in d:
            out[out.index(word)] = data[d.index(word.lower())]['forme1']

    return out

def convert_sentence(sentence):
    return convert(extractWords(sentence))
print(convert(extractWords('tous')))