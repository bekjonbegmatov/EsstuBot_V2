from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode

from data.databace import Users
from keyboards.inline.menu_inlie import select_week, days, menu_button
from data.databace import Users
from parcer.main import get_schedule
from parcer.wich_day import get_todays_data as todays_data_function

router = Router()

@router.callback_query(F.data == 'get_raspisaniya')
async def get_raspisaniya(call:CallbackQuery):
    await call.message.edit_text(text='⬇️ Выберите неделю ⬇️', reply_markup=select_week())

@router.callback_query(F.data.startswith('week_'))
async def week(call:CallbackQuery):
    wek = call.data.split('_')[1]
    await call.message.edit_text(text='⬇️ Выберите день ⬇️', reply_markup=days(week=int(wek)))

@router.callback_query(F.data.startswith('get_schedule_'))
async def parse_read(call:CallbackQuery):
    """ The callback for getting shedule from esstu.ru 
        this functino works the button bulder gets info abut day and week 
    """
    day = call.data.split('_')[2]
    wek = call.data.split('_')[3]
    print(call.data)
    day = 'day_' + day
    user_info = Users().chaeck_users(user_id=call.from_user.id)
    data = get_schedule(degre='bakalavr', course=str(user_info[4]), group=user_info[5])

    text = f"Расписание для : {data[day]['day']} неделя {wek} \n\n"
    for t in data[day]['data']:
        text += f"""┍<b>Время :</b> <code>{t['time']}</code>
├<b>Тип :</b> <code>{t['subject_type']}</code>
├<b>Придмет :</b> <code>{t['subject_name']}</code>
├<b>Преподаватель :</b> <code>{t['teacher_name']}</code>
└<b>Аудитория :</b> <code>{t['classroom']}</code>\n
"""
    if call.message.text != text: 
        await call.message.edit_text(text=text, reply_markup=days(week=wek), parse_mode=ParseMode.HTML)

@router.callback_query(F.data == "get_todays_data")
async def todays_data(call:CallbackQuery):
    user_info = Users().chaeck_users(user_id=call.from_user.id)
    text = todays_data_function(degre='bakalavr', course=str(user_info[4]), group=user_info[5])

    if call.message.text != text: 
        await call.message.edit_text(text=text, reply_markup=menu_button(), parse_mode=ParseMode.HTML)