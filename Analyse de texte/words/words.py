# from nltk.parse.generate import generate
from nltk.tokenize import word_tokenize
import nltk
import os, sys

#lire un fichier txt depuis le disque

def lecture(fichier):
    try:
        texte_fichier = open(fichier).read()
    except FileNotFoundError:
        return 'not found'
    return texte_fichier

def filtre(texte_parse):
    words = word_tokenize(texte_parse)
    return words

def pos_tag(words):
    name = []
    pos_tag_filter = nltk.pos_tag(words)
    for mot, tag in pos_tag_filter:
        if tag == 'NN':
            name.append(mot)

    return name

def file_save(name):
    resultat = open("noms.txt","w")
    for q in name:
        resultat.write(q)
        resultat.write(' ')
    resultat.close
    #for mot, tag in pos_tag_filter:
    #print(mot,tag)
    # return

def main(fichier):
    texte = lecture(fichier)
    tokenized_words = filtre(texte)
    nom = pos_tag(tokenized_words)
    resultat = file_save(nom)

if __name__ == "__main__":
    main(str(sys.argv[1]))

#pour executer le code sur le terminal : python words.py './lettres.txt'
