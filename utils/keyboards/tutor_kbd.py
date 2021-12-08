from aiogram import types

from utils.callback_factorys.tutor_callback import tutor_schedule_callback
from utils.misc.menu_utils import menu_str


def tutor_schedule_menu():
    k = types.InlineKeyboardMarkup()
    k.add(
        types.InlineKeyboardButton(menu_str['tutor-schedule-prev'], callback_data=tutor_schedule_callback(-1)),
        types.InlineKeyboardButton(menu_str['tutor-schedule-next'], callback_data=tutor_schedule_callback(1)),
    )
    return k
