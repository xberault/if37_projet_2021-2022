import json
import os

test = "Tous les artistes sont là"

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

def convert(splittedText, forme):
    out = splittedText
    d = getMascWords()
    for word in out:
        if word in d:
            out[out.index(word)] = data[d.index(word)][forme]
        elif word.lower() in d:
            out[out.index(word)] = data[d.index(word.lower())][forme].capitalize()
        
        elif (word[:-1] in d) and (word[-1]=='s'):
            out[out.index(word)] = data[d.index(word[:-1])][forme].capitalize() + 's'
        elif (word[:-1].lower() in d) and (word[-1]=='s'):
            out[out.index(word)] = data[d.index(word[:-1].lower())][forme].capitalize() + 's'

    return out

def convert_sentence(sentence, forme):
    return ' '.join(convert(extractWords(sentence), forme))

print(convert_sentence(test, 'forme1'))