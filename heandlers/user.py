from aiogram import Router
from aiogram.types import Message , ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.databace import Users
from keyboards.simple.user_r import course_button, group_button 
from keyboards.inline.menu_inlie import menu_button
from utils.user import UserInfo

from heandlers.functions import check_user_group
router = Router()

@router.message(UserInfo.degre)
async def get_degre(message:Message, state:FSMContext):
    if message.text == 'Бакалавриат, специалитет':
        await message.answer(text='Хорошо теперь выбирай свой курс : ', reply_markup=course_button())
        await state.update_data(degre=message.text)
        await state.set_state(UserInfo.course)
    else : await message.answer(text='Пожалуйста выбирай из списка ')
        
@router.message(UserInfo.course)
async def get_course(message:Message, state:FSMContext):
    if int(message.text) <= 4 :
        await message.answer(text='Хорошо теперь выбирай группу: ',reply_markup=group_button(kurs=message.text))
        await state.update_data(course=message.text)
        await state.set_state(UserInfo.group)
    else : await message.answer(text='Пожалуйста выбирай из списка ')

@router.message(UserInfo.group)
async def get_course(message:Message, state:FSMContext):
    data = await state.get_data()
    if check_user_group(kourse=data['course'], group=message.text):
        text = f'Uruvun : {data['degre']}\nKurs : {data['course']}\nGruppa : {message.text}\n\n'
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await state.clear()
        # Adding usert to db
        Users().create_user(
            user_id=message.chat.id,
            usename=message.from_user.username,
            degre=data['degre'],
            course=int(data['course']),
            grup=message.text
            )
        await message.answer(text='Выберите :', reply_markup=menu_button())
    else : await message.answer(text='Vibirete grupu : ')