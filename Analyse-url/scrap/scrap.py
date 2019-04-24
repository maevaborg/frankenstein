from bs4 import BeautifulSoup
import requests
from time import sleep
from time import time
from random import randint
from warnings import warn
import sys

def get_res(url, max_num):
    pages = [str(i) for i in list (range(1, max_num))]
    data = []
    print('start get {}'.format(url))

    for page in pages:
        requetes=0
        start_time = time()
        response = requests.get(url + 'page/' + page)
        sleep(randint(8,15))
        requetes+=1
        elapsed_time = time() - start_time

        print('status {}, page{}, requetes{}'.format(response.status_code, page, requetes))

        if response.status_code!= 200:
            warn('status {}, page {}, requetes {}'.format(response.status_code, page, requetes))
            continue
        if requetes > 50:
            break

        data.append(response.content)

    print('scrap{} end'.format(url))

    return(data)

def parse_page(page):
#prend un seul élément de la liste, et non l'ensemble de la liste

    #page = 'test'
    soup = BeautifulSoup(page,features="html.parser")
    post = soup.find_all(class_='post')
    # print(post)

    data = []

#permalink = sur le site, cela correspond à la date du post
#realpost = correspond au texte du post

    for i,p in enumerate(post):
        permalink = post[i].find(class_='permalink').text
        realpost = post[i].find(class_='realpost').text
        t = (permalink, realpost)
        data.append(t)

    return(data)

def save_file(data,name):

    print("start parse html")

    for item in data:
        resultat = parse_page(item)
        file = open(name + '.txt', 'a')
        for date, texte in resultat:
            file.write(date + texte)
        file.close()
    print("end save text")

def main(url, num_pages, name):
    pages = get_res(url, num_pages)
    # print(pages)
    save_file(pages,name)

if __name__== "__main__":
    main(str(sys.argv[1]),int(sys.argv[2]),str(sys.argv[3]))
