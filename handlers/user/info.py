from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.keyboards.info_kbd import get_price_kbd
from utils.letterings.info_lett import info_text, info_prices_text, err_get_price_text, get_price_text, \
    get_price_success_text, get_price_err_text
from utils.requests.users_reqests import UserRequest


async def guest_info(msg: types.Message):
    await msg.answer(info_text(), disable_web_page_preview=True)


async def guest_pricing(msg: types.Message):
    await msg.answer(await info_prices_text(), disable_web_page_preview=True)


async def guest_price_select(msg: types.Message, regexp_command=None):
    price_id = regexp_command.group(1)
    prices = await UserRequest.get_prices()
    p = next((x for x in prices if x['id'] == int(price_id)), False)
    if isinstance(p, dict):
        txt = get_price_text(p)
        keyboard = get_price_kbd(p)
    else:
        txt = err_get_price_text(price_id)
        keyboard = None
    await msg.answer(txt, reply_markup=keyboard)


async def guest_price_ordered(query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    price_id = int(callback_data['id'])
    cost = int(callback_data['cost'])
    user_id = query.message.chat.id
    r = await UserRequest.new_oder(price_id, cost, user_id, state)
    if r.get('success'):
        await query.message.edit_text(get_price_success_text())
    else:
        await query.answer(get_price_err_text())

