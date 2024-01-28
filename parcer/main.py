import parce_todo , parce_j
import json

"""
    THIS IS A MAIN PARSER FILE 

    WHAT THIS FILE DO
        This file cals an other parsing files and returns redy file 

    I'M SORRY FOR DESCRIPTION ;)

    USING 
        You can import thes file an use there 
        Call the function get_schedule 
            ARGUMENTS :
                degre - this is degre (for example Бакалавриат)
                course - this is a student course (for example 1)
                group - This is a group (for example Б743)
            RETURN
                Function can return False or Dictinary 

                False - this means no find this course or group
                Dictinary - This is raspisaniya 
"""

def get_schedule(degre:str, course:str, group:str):
    try:
        with open('data/json/groups_key.json', 'r') as f:
            data = json.load(f)
        id = data[degre][course][group]
        raspi = parce_todo.Schedule(schedule=id).save_schedule_to_json(filename='schedule.json')
        res = parce_j.get_schedule_file()
        return res

    except :
        return False
    
# print(get_schedule(degre='bakalavr', course='1', group='Б733-2'))
""" 
    SIMPLE USING :
    data = get_schedule(degre='bakalavr', course='1', group='Б743')

    [print(f'{data['day_1']['day']}\n{t['time']}\n{t['subject_type']}\n{t['subject_name']}\n{t['teacher_name']}\n{t['classroom']}\n') for t in data['day_1']['data']]
"""
