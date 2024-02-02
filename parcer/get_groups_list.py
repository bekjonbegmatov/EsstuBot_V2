import requests
from bs4 import BeautifulSoup
import json

""" THIS SCRIPT CAN GET ALL GROUPS ID AND SAVE TO FILES """

def get_list():
    """ AAAAAAAAAAAAAA BU MANI ULDIRIB QUYADI KUUUUUUUUUUUUUU !!!!!!
        I WAS STUPED END MAKE A MISTAKE I'M BROKEN AAAA
    """
    i = 208
    data = {}
    while i != 213 :
        res = requests.get(f'https://portal.esstu.ru/bakalavriat/{i}.htm').text
        soup = BeautifulSoup(res, 'lxml')
        data[soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = i
        print(f'[ INFO ] {soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')} : {i} , SAVED !')
        i+=1
    
    with open('groups_list.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

get_list()