from aiogram.utils.keyboard import InlineKeyboardBuilder

def menu_button():
    bulder = InlineKeyboardBuilder()
    bulder.button(text='👤Аккаунт👤' , callback_data="get_account")
    bulder.button(text='📝Pасписание📝' , callback_data="get_raspisaniya")
    return bulder.as_markup()

def profile():
    bulder = InlineKeyboardBuilder()
    bulder.button(text='✏️ Изменить ✏️' , callback_data="edit_profile")
    bulder.button(text='⬅️ Назад ⬅️' , callback_data="back_to_menu")
    bulder.button(text='📝 Pасписание 📝' , callback_data="get_raspisaniya")
    bulder.adjust(1,2)
    return bulder.as_markup()

# FOR GETTING RASPISANIYA

def select_week():
    bulder = InlineKeyboardBuilder()
    bulder.button(text='1️⃣' , callback_data="week_1")
    bulder.button(text='2️⃣' , callback_data="week_2")
    bulder.button(text='⬅️ Назад ⬅️' , callback_data="back_to_menu")
    bulder.adjust(2,1)
    return bulder.as_markup()

def days(week:int):
    bulder = InlineKeyboardBuilder()
    texts = ['1️⃣ понедельник', '2️⃣ вторник', '3️⃣ среда', '4️⃣ четверг', '5️⃣ пятница', '6️⃣ суббота']
    if week == 1:
        i = 1
        for day in texts:
            bulder.button(text=day , callback_data=f"get_schedule_{i}")
            i+=1
    else:
        i = 1
        for day in texts:
            bulder.button(text=day , callback_data=f"get_schedule_{i+6}")
            i+=1
    bulder.button(text='⬅️ Назад ⬅️' , callback_data="back_to_menu")
    bulder.adjust(2,2,2,1)
    return bulder.as_markup()