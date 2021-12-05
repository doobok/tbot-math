from aiogram import types

from utils.keyboards.global_kbd import main_menu
from utils.letterings.balance_lett import tutor_balance_text, tutor_zoom_text


async def tutor_balance(msg: types.Message) -> None:
    await msg.answer(await tutor_balance_text(msg.from_user.id), reply_markup=main_menu())


async def tutor_zoom(msg: types.Message) -> None:
    await msg.answer(await tutor_zoom_text(msg.from_user.id), reply_markup=main_menu(), disable_web_page_preview=True)


