from aiogram.fsm.state import StatesGroup , State 

class UserInfo(StatesGroup):
    """ THIS IS A STATE FOR GETING USER INFO """
    degre = State()
    course = State()
    group = State()

class UserInfoUpdate(StatesGroup):
    """ THIS IS A STATE FOR UPDATING/EDIT/CHANGE USER INFO """
    degre = State()
    course = State()
    group = State()

# class Chat