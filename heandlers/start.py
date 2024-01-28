from aiogram import Router
from aiogram.types import Message 
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

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

@router.message(Command('help'))
async def help_command(message:Message):
    await message.bot.send_message(chat_id=message.chat.id, text='this is a help menu')

router.include_routers(
    user_router
)