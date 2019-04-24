#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importing the libraries
from bs4 import BeautifulSoup
import requests
import sys

#lire le contenu en html brut via une url
def get_data(url):
  result = requests.get(url)
  return(result.content)

#filtrer le contenu 
def parse_html(data, balise):
  resultat_parse = BeautifulSoup(data, 'html.parser')
  balise_html = resultat_parse.find_all(balise)
  return(balise_html)

#sauvegarder le contenu parsé dans un fichier texte 
def save_text(html):
 # print('save texte', html)
  resultat_balise = open('balise.txt',"w", encoding='utf-8')
  for q in html:
    if q.string is not None:
      resultat_balise.write(q.string)
  resultat_balise.close()

#fonction principale
def main(url, balise):
  data = get_data(url)
  html_balise = parse_html(data, balise)
  save_text(html_balise)

#lors de l'ecriture dans le terminal, 1 = url 2= balise $ python balise.py 'https://www.franceculture.fr/recherche/articles-et-diffusions?q=mary+shelley' 'p'
if __name__ == "__main__":
  main(str(sys.argv[1]), str(sys.argv[2]))

# test erreur
#def lecture(fichier):
    #try:
        #texte_fichier = open(fichier).read()
    #except FileNotFoundError:
        #return 'not found'
    #return texte_fichier

    "https://en.wikipedia.org/wiki/Frankenstein" 'p'