from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from utils.callback_factorys.guest_callback import get_order_callback
from utils.callback_factorys.tutor_callback import tutor_schedule_callback
from utils.misc.menu_utils import menu_str
from .balance import tutor_balance, student_balance
from .help import bot_help
from .info import guest_info, guest_pricing, guest_price_select, guest_price_ordered
from .schedule import st_lesson_history, st_pass_history, st_schedule, st_zoom_url, tutor_zoom, tutor_schedule, \
    tutor_schedule_switch
from .start import bot_start, main_menu
from .contact import bot_contact


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart(), state="*")
    dp.register_message_handler(bot_help, CommandHelp(), state="*")
    dp.register_message_handler(bot_contact, content_types='contact', state="*")

    dp.register_message_handler(main_menu, text=[menu_str['main-menu']], state="*")

    dp.register_message_handler(st_schedule, text=[menu_str['student-schedule']], state="*")
    dp.register_message_handler(st_zoom_url, regexp_commands=['online_([0-9]*)'], state="*")
    dp.register_message_handler(student_balance, text=[menu_str['student-balance']], state="*")
    dp.register_message_handler(st_lesson_history, text=[menu_str['student-lessons-history']], state="*")
    dp.register_message_handler(st_pass_history, text=[menu_str['student-pass-history']], state="*")

    dp.register_message_handler(tutor_schedule, text=[menu_str['tutor-schedule']], state="*")
    dp.register_message_handler(tutor_balance, text=[menu_str['tutor-balance']], state="*")
    dp.register_callback_query_handler(tutor_schedule_switch, tutor_schedule_callback(None), state="*")
    dp.register_message_handler(tutor_zoom, text=[menu_str['tutor-zoom']], state="*")

    dp.register_message_handler(guest_info, commands=['info'], state="*")
    dp.register_message_handler(guest_pricing, commands=['pricing'], state="*")
    dp.register_message_handler(guest_price_select, regexp_commands=['price_([0-9]*)'], state="*")
    dp.register_callback_query_handler(guest_price_ordered, get_order_callback(None, None), state="*")

