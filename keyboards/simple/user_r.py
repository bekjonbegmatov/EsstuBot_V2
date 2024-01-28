from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import json
def level_button():
    with open(file='data/json/user_r.json', mode='r') as f:
        data = json.load(f)
    builder = ReplyKeyboardBuilder()
    for k,v in data['level'].items():
        builder.add(KeyboardButton(text=v))
    builder.adjust(1)
    return builder.as_markup()

def course_button():
    with open(file='data/json/user_r.json', mode='r') as f:
        data = json.load(f)
    builder = ReplyKeyboardBuilder()
    for k,v in data['kourse'].items():
        builder.add(KeyboardButton(text=str(v)))
    builder.adjust(2,2)
    return builder.as_markup()

def group_button(kurs:str):
    with open(file='data/json/groups_key.json', mode='r') as f:
        data = json.load(f)
    builder = ReplyKeyboardBuilder()
    for k,v in data['bakalavr'][str(kurs)].items():
        builder.add(KeyboardButton(text=k))
    builder.adjust(3)
    return builder.as_markup()
# level_button()