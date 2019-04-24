#Analyse d'une url
#Librairies utilisées : bs4, beautifulsoup, requests, time, random, warning, sys

from bs4 import BeautifulSoup
import requests
from time import sleep
from time import time
from random import randint
from warnings import warn
import sys

#
def get_res(url, max_num):
    pages = [str(i) for i in list (range(1, max_num))]
    data = []
    print('start get {}'.format(url))

    #
    for page in pages:
        requetes=0
        start_time = time()
        response = requests.get(url + 'page/' + page)
        sleep(randint(8,15))
        requetes+=1
        elapsed_time = time() - start_time

        print('status {}, page{}, requetes{}'.format(response.status_code, page, requetes))

        #Conditions : ??? et ?? 
        if response.status_code!= 200:
            warn('status {}, page {}, requetes {}'.format(response.status_code, page, requetes))
            continue
        if requetes > 50:
            break

        data.append(response.content)

    print('scrap{} end'.format(url))

    return(data)

#Fonction pour ne prendre qu'un élément de la liste, et non l'ensemble de la liste
def parse_page(page):

    #page = 'test'
    soup = BeautifulSoup(page,features="html.parser")
    post = soup.find_all(class_='post')
    # print(post)

    data = []

#permalink = sur le site, cela correspond à la date du post
#realpost = correspond au texte du post

# Boucle pour énumérer les posts
    for i,p in enumerate(post):
        permalink = post[i].find(class_='permalink').text
        realpost = post[i].find(class_='realpost').text
        t = (permalink, realpost)
        data.append(t)

    return(data)

#Fonction pour créer un nvx fichier, stocker les données et fermer le fichier
def save_file(data,name):

    print("start parse html")

    #Boucle qui ouvre le fichier, stocke et ferme
    for item in data:
        resultat = parse_page(item)
        file = open(name + '.txt', 'a')
        for date, texte in resultat:
            file.write(date + texte)
        file.close()
    print("end save text")

#Fonction principale
def main(url, num_pages, name):
    pages = get_res(url, num_pages)
    # print(pages)
    save_file(pages,name)


#Lors de l'ecriture dans le terminal, 1 = ? /  2= ? / 3= ?
if __name__== "__main__":
    main(str(sys.argv[1]),int(sys.argv[2]),str(sys.argv[3]))
