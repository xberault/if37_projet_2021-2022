import json

test = "Tous les acheteur"

with open(__file__.replace("convert.py", "dico.json")) as f:
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

print(convert(extractWords(test)))