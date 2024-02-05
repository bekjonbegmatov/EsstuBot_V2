import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

class ESSTU_New:
    """ This Class for parsing news from esstu.ru 
        Ussage : 
            methods :
                is_any_news - returns :
                    True if new has been found
                    False if new hasn't found
                get_data - returns :
                    Dict - data
                Call only if is_any_news returnded Trus
    """
    def __init__(self) -> None:
        pass

    def __get_last_id(self) -> int:
        """ This metod for getting last id from file (data/txt/last_news_id.txt) """
        with open('data/txt/last_news_id.txt', 'r') as f:
            return int(f.read())
    def __set_new_id(self) -> bool:
        """ This method for uploading a new value of new id ~__get_last_id """
        with open('data/txt/last_news_id.txt', 'w') as f:
            f.write(str(self.target_new_id))
        return True
    
    def __get_id_from_esstu(self) -> int:
        """ This method gets last id of news from essti.ru and returns """
        res = requests.get('https://esstu.ru/uportal/news/allNews.htm?showOnIndex=true&categoryId=2').text
        soup = BeautifulSoup(res, 'lxml')
        news = soup.find_all('div', {"class" : "allNewsItem"})[0]
        id_ = news.find_all('a', {"class" : "newsImageLink"})[0]["href"]
        return int(id_.split('=')[1])
    
    def __parce_news_page(self) -> dict:
        """ This method for Parsing data from esstu.ru, this method parce data and returns dict"""

        # Getting HTML data
        url = f"https://esstu.ru/uportal/faculties/viewNews.htm?newsId={self.target_new_id}"
        res = requests.get(url=url).text
        # Creating Soup 
        soup = BeautifulSoup(res, 'lxml')
        # Parsing data 
        title = soup.find('h1', {"class" : "bodyTitle cntr"}).text.strip()
        img = soup.find_all("img", {"class" : "allNewsItemImg"})[0]["src"]
        typeName = soup.find('div', {"class" : "newsTypeName"}).text
        des1 = soup.find_all("span", {"style" : "font-family: arial, helvetica, sans-serif; font-size: 12pt;"})[0].text
        des2 = soup.find_all("span", {"style" : "font-family: arial, helvetica, sans-serif; font-size: 12pt;"})[1].text
        info = soup.find("div", {"class" : "c5"}).get_text().strip().split('  ')[0]
        data = {
            "title" : title,
            "img" : img,
            "type" : typeName,
            "des1" : des1,
            "des2" : des2,
            "info" : info,
            "url" : url
        }

        self.image_url = img
        return data

    def download_image(self) -> str:
        """ This method downloads image and returns full path of image """
        url = f"https://esstu.ru{self.image_url}"
        req = requests.get(url=url, allow_redirects=True).content
        with open('data/img/news.png', 'wb') as handler:
            handler.write(req)
        return os.getcwd() + "/data/img/news.png"
        # return url
        
    def is_any_news(self) -> bool:
        """ The method for checking for any news in esstu.ru"""
        last_id = self.__get_last_id()
        last_new_id = self.__get_id_from_esstu()
        if last_id != last_new_id:
            self.target_new_id = last_new_id
            return True
        return False
        
    def get_data(self) -> dict:
        """ This method for getting data from esstu.ru please use pas is any news """
        data = self.__parce_news_page()
        self.__set_new_id()
        return data

""" 
    Simple ussage :
    
esstu = ESSTU_New()
if esstu.is_any_news():
    print(esstu.get_data())
"""
