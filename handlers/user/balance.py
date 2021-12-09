from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.keyboards.global_kbd import main_menu
from utils.keyboards.student_kbd import st_balance_menu
from utils.letterings.balance_lett import tutor_balance_text, student_balance_text


async def tutor_balance(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(await tutor_balance_text(msg.from_user.id, state), reply_markup=main_menu())


async def student_balance(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(await student_balance_text(msg.from_user.id, state), reply_markup=st_balance_menu())

