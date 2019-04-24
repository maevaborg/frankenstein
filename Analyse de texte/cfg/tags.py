#Ce code ouvre un fichier depuis l'ordinateur, tokenize le texte jusqu'a 20 charactères
#puis
# Librairies utilisées : 
# NLTK,Gutenberg, tokenize, stopwords, regex


import nltk
from nltk.corpus import gutenberg
from nltk.tokeninze import word_tokenize, sent tokeninze
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#ouvrir un document via la librairie gutenberg + ne lit que 20 charactères
gutenberg.filieds()
text = gutemberg.rax('text.txt')
text [0:20]

#Tokenisation du texte 
words = word_tokenize(text)
words[:20]

#stopwords ? 
test = 'this is a sentence this is a very good sentence'
stop_words = set(stopwords.words('english'))
words_test = words_tokenize(test)
filtre_test = []
for w in words_test:
    if w not in stop_words:
        filtre_test.append(w)

#filtrer le texte avec le Part Of Speech 
filtre_test
pos_tag_test = nltk.pos_tag(filtre_test)
pos_tag_test

filtre_test = []

#Création d'une boucle pour... ?
for w in words:
    w = w.lower()
    if w not in stop_words:
        filtre_text.append(w)

len(filtre_text)

tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(text)
filtre_text = []

type(filtre_text)

pos_tag_text = nltk.pos_tag(filtre_set)
type(pos_tag_text[0])

#Classer les mots et tags dans le texte
for (mot, tag) in pos_tag_text:
    print(mot, tag)

noms = []

for mot, tag in pos_tag_text:
    if tag == 'NN':
        noms.append(mot)

noms
len(noms)
noms_str='NN ->'

# Boucle pour faire le tri des charactères inutiles, espaces
for n in noms:
     noms_str += "'" + n + "'" + " | "
     noms_str[:20]
     noms_str = noms_str[:-3]
     noms_str = noms_str.replace(u'\xa0', ' ')
     #print(noms_str)

#créer un nouveau fichier, ouvrir, stocker et fermer le fichier 
file = open('noms.txt','w')
file.write(noms_str)
file.close()
print("end save text")
