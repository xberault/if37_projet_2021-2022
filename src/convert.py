import json
import os


### Formes utilisées pour traduire d'une différente manière les phrases
FORME_CONTRACTEE = 'forme1'
FORME_LONGUE = 'forme2'
FORME_COURTE = 'forme3'
FORME_4 = 'forme4'

FORME_DEFAULT = FORME_CONTRACTEE

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
    import re

    phrases = sentence.splitlines(True)
    res = ""
    for p in phrases:
        #p[-1] est le délimiteur de ligne, cela permet de garder l'indentation originale
        res += " ".join(convert(extractWords(p[:-1]), forme)) + p[-1]
    return res



if __name__ == "__main__":
    test = "Tous les artistes sont là"
    print(convert_sentence(test, FORME_DEFAULT))