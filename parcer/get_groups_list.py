import requests
from bs4 import BeautifulSoup
import json

""" THIS SCRIPT CAN GET ALL GROUPS ID AND SAVE TO FILES """

def get_list():
    """ AAAAAAAAAAAAAA BU MANI ULDIRIB QUYADI KUUUUUUUUUUUUUU !!!!!!
        I WAS STUPED END MAKE A MISTAKE I'M BROKEN AAAA
    """
    i = 1
    data = {"1" : {}, "2" : {}, "3" : {}, "4": {}, "5" : {}}
    while i != 214 :#214 :
        res = requests.get(f'https://portal.esstu.ru/bakalavriat/{i}.htm').text
        soup = BeautifulSoup(res, 'lxml')
        if i <= 52 : data["1"][soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = f'https://portal.esstu.ru/bakalavriat/{i}.htm'
        elif i > 52 and i <= 107 : data['2'][soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = f'https://portal.esstu.ru/bakalavriat/{i}.htm'
        elif i > 107 and i <= 153 : data['3'][soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = f'https://portal.esstu.ru/bakalavriat/{i}.htm'
        elif i > 153 and i <= 209 : data['4'][soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = f'https://portal.esstu.ru/bakalavriat/{i}.htm'
        elif i > 209 and i <= 213 : data['5'][soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = f'https://portal.esstu.ru/bakalavriat/{i}.htm'
        
        # data[soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')[1:]] = i
        print(f'[ INFO ] {soup.find_all('font')[1].get_text().encode("latin-1").decode('cp1251')} : {f'https://portal.esstu.ru/bakalavriat/{i}.htm'} , SAVED !')
        i+=1
    
    with open('groups_list.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

get_list()