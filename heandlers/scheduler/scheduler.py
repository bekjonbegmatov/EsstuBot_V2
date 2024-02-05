from aiogram import Bot
from data.databace import Users
from parcer.wich_day import get_todays_data as todays_data_function , get_tomorows_data
from keyboards.inline.menu_inlie import menu_button
from aiogram.enums.parse_mode import ParseMode

async def send_todays_data(bot:Bot):
    all_users = Users().get_all_users()
    for user in all_users:
        try :
            text = "Расписание для сегодня 🫣\n" + todays_data_function(degre='bakalavr', course=str(user[4]), group=user[5])
            await bot.send_message(chat_id=user[1], text=text, reply_markup=menu_button(), parse_mode=ParseMode.HTML)
        except :
            # print('Bot Bloked by user')
            pass

async def send_tomorows_data(bot:Bot):
    all_users = Users().get_all_users()
    for user in all_users:
        try:
            text = "Расписание для завтра 🫣\n" + get_tomorows_data(degre='bakalavr', course=str(user[4]), group=user[5])
            await bot.send_message(chat_id=user[1], text=text, reply_markup=menu_button(), parse_mode=ParseMode.HTML)
        except:
            pass