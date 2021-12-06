from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from utils.callback_factorys.guest_callback import get_order_callback
from utils.misc.menu_utils import menu_str
from .balance import tutor_balance, tutor_zoom, student_balance
from .help import bot_help
from .info import guest_info, guest_pricing, guest_price, ordered_price
from .schedule import st_lesson_history, st_pass_history, st_schedule
from .start import bot_start, main_menu
from .contact import bot_contact


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(bot_contact, content_types='contact')

    dp.register_message_handler(main_menu, text=[menu_str['main-menu']])

    dp.register_message_handler(st_schedule, text=[menu_str['student-schedule']])
    dp.register_message_handler(student_balance, text=[menu_str['student-balance']])
    dp.register_message_handler(st_lesson_history, text=[menu_str['student-lessons-history']])
    dp.register_message_handler(st_pass_history, text=[menu_str['student-pass-history']])

    dp.register_message_handler(tutor_balance, text=[menu_str['tutor-balance']])
    dp.register_message_handler(tutor_zoom, text=[menu_str['tutor-zoom']])

    dp.register_message_handler(guest_info, commands=['info'])
    dp.register_message_handler(guest_pricing, commands=['pricing'])
    dp.register_message_handler(guest_price, regexp_commands=['price_([0-9]*)'])
    dp.register_callback_query_handler(ordered_price, get_order_callback(None, None))

