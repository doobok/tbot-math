from aiogram import types

from utils.callback_factorys.guest_callback import get_order_callback


def get_price_kbd(p):
    k = types.InlineKeyboardMarkup()
    price_id = p.get('id')
    cost = p.get('price') * p.get('count')
    return k.add(types.InlineKeyboardButton('🎁 Замовити', callback_data=get_order_callback(price_id, cost)))
