from aiogram import types

from utils.callback_factorys.guest_callback import get_order_callback
from utils.misc.menu_utils import menu_str


def get_price_kbd(p):
    k = types.InlineKeyboardMarkup()
    price_id = p.get('id')
    cost = p.get('price') * p.get('count')
    return k.add(types.InlineKeyboardButton(menu_str['to-order'], callback_data=get_order_callback(price_id, cost)))
