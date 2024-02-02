from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode

from data.databace import Users
from keyboards.inline.menu_inlie import profile, menu_button
# Importing callbacks for getting schedule
from callback.raspisaniya_call import router as schedule_call_router

router = Router()

@router.callback_query(F.data == 'back_to_menu')
async def back_to_menu(call:CallbackQuery):
    await call.message.edit_text(text='Выбирай', reply_markup=menu_button())

@router.callback_query(F.data.startswith('get_account'))
async def get_account(call:CallbackQuery):
    user_id = call.from_user.id

    user_info = Users().chaeck_users(user_id=user_id)
    text = f"""👤 Профил 👤
├ID : <code>{user_id}</code>
├{user_info[3]}
├Курс : <code>{user_info[4]}</code>
└Группа : <code>{user_info[5]}</code>
"""
    await call.message.edit_text(text=text, reply_markup=profile(), parse_mode=ParseMode.HTML)


router.include_router(schedule_call_router)