from aiogram import Router, F
from aiogram.types import Message , ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext

from data.databace import Users
from keyboards.simple.user_r import course_button, group_button , level_button
from keyboards.inline.menu_inlie import menu_button
from utils.user import UserInfo , UserInfoUpdate

from heandlers.functions import check_user_group
from callback.menu_inline_callback import router as user_call_router
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
        text = f"Ваш акаунт : \n{data['degre']}\nКурс : {data['course']}\nГруппа : {message.text}\n\n"
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
    else : await message.answer(text='Пожалуйста выбирай из списка')


# This functions for changing user data

@router.callback_query(F.data == 'edit_profile')
async def edit_profile(call:CallbackQuery, state:FSMContext):
    await state.set_state(UserInfoUpdate.degre)
    await call.message.delete()
    await call.message.bot.send_message(chat_id=call.from_user.id, text='Выбирай', reply_markup=level_button())
    # await call.message.edit_text(text='Выбирай :',reply_markup=level_button())

@router.message(UserInfoUpdate.degre)
async def get_updated_degre(message:Message, state:FSMContext):
    if message.text == 'Бакалавриат, специалитет':
        await message.answer(text='Хорошо теперь выбирай свой курс : ', reply_markup=course_button())
        await state.update_data(degre=message.text)
        await state.set_state(UserInfoUpdate.course)
    else : await message.answer(text='Пожалуйста выбирай из списка ')
    
@router.message(UserInfoUpdate.course)
async def get_course(message:Message, state:FSMContext):
    if int(message.text) <= 4 :
        await message.answer(text='Хорошо теперь выбирай группу: ',reply_markup=group_button(kurs=message.text))
        await state.update_data(course=message.text)
        await state.set_state(UserInfoUpdate.group)
    else : await message.answer(text='Пожалуйста выбирай из списка ')

@router.message(UserInfoUpdate.group)
async def get_course(message:Message, state:FSMContext):
    data = await state.get_data()
    if check_user_group(kourse=data['course'], group=message.text):
        text = f"Uruvun : {data['degre']}\nKurs : {data['course']}\nGruppa : {message.text}\n\n"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await state.clear()
        # Adding usert to db
        Users().update_user_data(
            user_id=message.chat.id,
            degre=data['degre'],
            course=int(data['course']),
            grup=message.text
            )
        await message.answer(text='Выберите :', reply_markup=menu_button())

    else : await message.answer(text='Пожалуйста выбирай из списка')


router.include_router(user_call_router)

