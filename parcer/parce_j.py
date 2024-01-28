import re
import json

"""
    THIS FILE USES RE FOR FILTRING ELEMENTS FROM JSON FILE 
    FOR EXAMPLE 
    IF I HAVE 
    "day": "Пнд",
    "schedule": [
      {
        "time": "09:00-10:35",
        "subject": "_"
      },
      {
        "time": "10:45-12:20",
        "subject": "лек.Объектно-ориентированное программирование ХАПТАХАЕВА Н.Б.  а.1-50 и/д"
      },
      {
        "time": "13:00-14:35",
        "subject": "лек.Дискретная математика ЧИМИТОВА Е.Г.  а.1-37 и/д"
      }
    THIS FILE TEKES ME 

    Пнд
    Time : 10:45-12:20
    Type : лек
    Subject : Объектно-ориентированное программирование
    Techer : ХАПТАХАЕВА Н.Б.
    clasroom : а.1-50

    Time : 13:00-14:35
    Type : лек
    Subject : Дискретная математика
    Techer : ЧИМИТОВА Е.Г.
    clasroom : а.1-37
"""

def process_schedule(schedule_data):
    res = {}
    i = 1
    for day_schedule in schedule_data:
        temp = {"day": day_schedule['day'], "data": []}
        for entry in day_schedule['schedule']:
            if entry['subject'] in ['_', '']:
                continue
            
            time = entry['time']
            subject_info = entry['subject']
            
            match = re.match(r'(?P<type>лек\.|пр\.|лаб\.)?\s*(?P<subject>.*?)\s+(?P<teacher>[А-ЯЁ].*?)\s*(?P<classroom> а\.\S+)?$', subject_info)
            
            if match:
                
                subject_type = match.group('type') or ""
                subject_name = match.group('subject') or ""
                teacher_name = match.group('teacher') or ""
                classroom = match.group('classroom') or ""
                t_data = {
                    "time": time.strip(),
                    "subject_type": subject_type.strip(),
                    "subject_name": subject_name.strip(),
                    "teacher_name": teacher_name.strip(),
                    "classroom": classroom.strip()
                }
                temp["data"].append(t_data)      
        res[f"day_{str(i)}"] = temp
        i+=1

    return res

def get_schedule_file():
    """ THIS FUNCTION GETS DATA FROM FILE """
    with open('schedule.json', 'r', encoding='utf-8') as f:
        schedule_data = json.load(f)
    data = process_schedule(schedule_data)
    return data
def get_schedule(data):
    """ THIS FUNCTION GETS DATA FROM ATRIBUTE DATA"""
    return process_schedule(data)


# [print(f'{data['day_1']['day']}\n{t['time']}\n{t['subject_type']}\n{t['subject_name']}\n{t['teacher_name']}\n{t['classroom']}\n') for t in data['day_1']['data']]

