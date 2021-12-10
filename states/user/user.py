from aiogram.dispatcher.filters.state import State, StatesGroup


class BalanceRefill(StatesGroup):
    enter_sum = State()
    confirm_sum = State()
