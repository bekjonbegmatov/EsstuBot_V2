from aiogram import Router
from aiogram.types import Message 
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

# Import state
from utils.user import UserInfo
# Import an other Routers
from heandlers.user import router as user_router

# Import DATABESE manager
from data.databace import Users
from keyboards.simple.user_r import level_button
from keyboards.inline.menu_inlie import menu_button

router = Router()

@router.message(Command('start'))
async def start_message(message:Message, state:FSMContext):
    user = Users().chaeck_users(user_id=message.chat.id)
    if user == False:
        await message.reply(f'Здраствуйте, {message.from_user.first_name} !\nДобро пожаловат в Расписания бот.\nПочемуто я немогу вас узнать давайте посмотрим расписания :)')
        await state.set_state(UserInfo.degre)
        await message.answer(text='Пожалуста выберите : ', reply_markup=level_button())
    else :
        text = f'Привет {message.from_user.first_name} !\nЯ помню тебя.\nДумаю что эти данные ещё актуален : \n{user[3]}\nКурс : {user[4]}\nГруппа : {user[5]}.\nВыбирай'
        await message.answer(text=text, reply_markup=menu_button())

@router.message(Command('menu'))
async def back_to_menu(message:Message):
    await message.answer(text='Выбирай', reply_markup=menu_button())

@router.message(Command('help'))
async def help_command(message:Message):
    text = """🏫 ВСГУТУ Расписание Бот

💫Создатель студент первого курса, ИCиТ <b>Бегматов Бехруз 🥵</b>

🔍 Нашли <b>баг или ошибку</b> сообщите по этому адресу :
📎 https://github.com/bekjonbegmatov/EsstuBot_V2/issues

📨 Этот проект является открытием и вы можете <b>добавить</b> свои улучшения
📥 : https://github.com/bekjonbegmatov/EsstuBot_V2

🤫 А также первая версия бота, <b>PS: Работает исключительно для одного группы</b>
📎 https://github.com/bekjonbegmatov/esstu_bot
"""
    await message.bot.send_message(chat_id=message.chat.id, text=text , parse_mode=ParseMode.HTML)

router.include_routers(
    user_router,
)