import json
import os

from PIL.Image import NONE
import spacy

nlp = spacy.load("fr_core_news_sm")

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

def check_voisin(token, prev_token, next_token):
    """
    Verifie les voisins immédiats du mot et renvoie un booléen sur s'il doit être neutralisé ou non
    """
    d = getMascWords()

    next_mot = "" if next_token == None else next_token.text
    prev_mot = "" if prev_token == None else prev_token.text
    
    

    next_ok = next_mot.strip() == "" or next_mot.lower() in d
    
    prev_ok = prev_mot.strip() == "" or prev_mot.lower() in d
    
    adp_into_noun_ok = next_token == None or (str(next_token.pos_) == "NOUN" and str(token.pos_) == "ADP" and str(prev_token.pos_) == "NOUN")
    
    
    isOk = ((next_ok and prev_ok) or (str(token.pos_) != "DET"  and adp_into_noun_ok))
    return isOk or (prev_mot.lower() in d and str(token.pos_) == "NOUN")

def get_next_prev_mot(out, i):
    prev, next_t = None, None
    if i != 0:
        prev = out[i - 1]
    if i < len(out) - 1:
        next_t = out[i + 1]
    return [prev, next_t]

def convert(splittedText, forme, doc):
    out = splittedText
    d = getMascWords()
    
    print("-----------------")
    print("Txt: " + str(splittedText))
    

    for i in range(len(out)):
        word = out[i]
        
        token = doc[i]
        print(i, word)
        prev_mot, next_mot = get_next_prev_mot(doc, i)
        
        if word in d and check_voisin(token, prev_mot, next_mot):
            out[out.index(word)] = data[d.index(word)][forme]
        elif word.lower() in d and check_voisin(token, prev_mot, next_mot):
            out[out.index(word)] = data[d.index(word.lower())][forme].capitalize()
        elif (word[:-1] in d) and (word[-1]=='s'):
            out[out.index(word)] = data[d.index(word[:-1])][forme] + 's'
        elif (word[:-1].lower() in d) and (word[-1]=='s'):
            out[out.index(word)] = data[d.index(word[:-1].lower())][forme].capitalize() + 's'

        #conjuguaison (WIP)
        if word[-1:]=='é':
            out[out.index(word)] += "\u2027ée"
        if word[-2:]=='és':
            out[out.index(word)] += "\u2027ées"

    print("res : "  + str(out))
    return out

def addWord(masc, fem, forme1, forme2, forme3, forme4):
    data.append({
            'MASC': masc,
            'FEM': fem,
            'forme1': forme1,
            'forme2': forme2,
            'forme3': forme3,
            'forme4': forme4
        })
    with open(__file__.replace("convert.py", data_file), 'w') as out:
        json.dump(data, out)


def convert_sentence(sentence, forme):

    
        # Retourner les étiquettes de chaque token
        
    #doc = nlp(sentence)
    doc = nlp(sentence)
    
    phrases = sentence.splitlines(True)
    res = ""

    for i, sent in enumerate(doc.sents): #, p, token in enumerate(zip(phrases, doc)):
        #p[-1] est le délimiteur de ligne, cela permet de garder l'indentation originale lorsque présente
        
        p = [""] if i >= len(phrases) else phrases[i] + " "

            
        print("----- p:")
        print(str(sent))
        print(p)
        words = list(X.text for X in sent)
        print(str(words))
        print(list(sent))
        
        res += " ".join(convert(words, forme,sent))
        
        # permet de remttre l'indentation lors du copier/coller / retour à la ligne
        res += p[-1]
        
    #return [res] + [(X, X.pos_, X.morph) for X in doc] + [(X.text, X.label_) for X in doc.ents]
    return res



if __name__ == "__main__":
    ens_test = {
        """
chien
Cet apiculteur récolte du miel.
Le professeur écrit sur le tableau
Le pendentif est joli
Ceci est un travail du professeur.
Marseille est une belle ville.
        """
    }
    res_final = ""
    for test in ens_test:
        res_final += convert_sentence(test, FORME_DEFAULT) + "\n"
    print(res_final)
