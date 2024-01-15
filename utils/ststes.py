from aiogram.fsm.state import State, StatesGroup

class FormADM(StatesGroup):
    last_name = State()
    first_name = State()
    date_happy_birthday = State()
    filial = State()

class IT_Support_FST(StatesGroup):
    name_user = State()
    info_step = State()