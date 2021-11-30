from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp, IsSenderContact, ContentTypeFilter
from aiogram.types import ContentType

from .help import bot_help
from .info import guest_info, guest_pricing, guest_price
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
    dp.register_message_handler(guest_price, commands=['price'])

    # dp.register_message_handler(bot_contact, content_types=types.ContentTypes.CONTACT)

    # dp.message_handler(bot_contact, ContentTypeFilter(ContentType.CONTACT))
    # dp.register_message_handler(bot_another)

    # worked
    # dp.register_message_handler(bot_query_another, content_types=types.ContentTypes.PHOTO)
    # dp.register_message_handler(bot_query_another, content_types=types.ContentTypes.ANY)
