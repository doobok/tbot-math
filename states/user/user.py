from aiogram.dispatcher.filters.state import State, StatesGroup


class TutorSchedule(StatesGroup):
    schedule_nav = State()


class MainState(StatesGroup):
    role = State()
    role_id = State()
