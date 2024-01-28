from aiogram.fsm.state import StatesGroup , State 

class UserInfo(StatesGroup):
    """ THIS IS A STATE FOR GETING USER INFO """
    degre = State()
    course = State()
    group = State()