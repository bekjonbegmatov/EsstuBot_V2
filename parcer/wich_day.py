import requests 
from datetime import datetime
from bs4 import BeautifulSoup

from parcer import main

def wich_day_is_it():
    url = "https://www.esstu.ru/index.htm"
    response = requests.get(url=url).text
    soup = BeautifulSoup(response, 'lxml')
    wek = soup.find("span", {"class": "header-date"}).get_text()
    if len(wek.split('_')[-1]) == 1 : return '1'
    return '2'

def get_todays_data(degre:str, course:str, group:str):
    today = datetime.now()
    
    wek = wich_day_is_it()
    day = 'day_'+str(today.weekday()+1)
    if wek == '2':
        day = 'day_'+str(today.weekday()+7)

    data = main.get_schedule(degre=degre, course=course, group=group)
    text = f'Расписание для : {data[day]['day']} неделя {wek} \n\n'
    for t in data[day]['data']:
        text += f"""┍<b>Время :</b> <code>{t['time']}</code>
├<b>Тип :</b> <code>{t['subject_type']}</code>
├<b>Придмет :</b> <code>{t['subject_name']}</code>
├<b>Преподаватель :</b> <code>{t['teacher_name']}</code>
└<b>Аудитория :</b> <code>{t['classroom']}</code>\n
"""
    return text

# print(get_todays_data(degre='bakalavr', course='1', group='Б743'))






    