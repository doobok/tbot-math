from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from utils.callback_factorys.guest_callback import get_order_callback
from .help import bot_help
from .info import guest_info, guest_pricing, guest_price, ordered_price
from .start import bot_start
from .contact import bot_contact
from .another import bot_another
from .querydefault import bot_query_another


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(bot_contact, content_types='contact')

    dp.register_message_handler(guest_info, commands=['info'])
    dp.register_message_handler(guest_pricing, commands=['pricing'])
    dp.register_message_handler(guest_price, regexp_commands=['price_([0-9]*)'])
    dp.register_callback_query_handler(ordered_price, get_order_callback(None, None))

