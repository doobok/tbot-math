from aiogram.dispatcher.filters.state import State, StatesGroup


class TutorSchedule(StatesGroup):
    schedule_nav = State()
