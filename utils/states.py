from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):
    start = State()
    auth_username = State()
    auth_password = State()
    access = State()

    edit_name = State()
    edit_birthdate = State()
    edit_tel = State()
    edit_username = State()
    edit_email = State()
