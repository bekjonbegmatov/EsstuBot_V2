from aiogram.utils.keyboard import InlineKeyboardBuilder

def menu_button():
    bulder = InlineKeyboardBuilder()
    bulder.button(text='👤Аккаунт👤' , callback_data="get_account")
    bulder.button(text='📝Pасписание📝' , callback_data="get_raspisaniya")
    return bulder.as_markup()