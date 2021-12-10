from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.keyboards.global_kbd import main_menu
from utils.keyboards.student_kbd import st_balance_menu, st_balance_cancel
from utils.letterings.balance_lett import tutor_balance_text, student_balance_text, enter_balance_text, \
    enter_balance_sum_text, confirm_balance_text


async def tutor_balance(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(await tutor_balance_text(msg.from_user.id, state), reply_markup=main_menu())


async def student_balance(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(await student_balance_text(msg.from_user.id, state), reply_markup=st_balance_menu())


async def st_balance_refill(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(await enter_balance_text(state), reply_markup=st_balance_cancel())


async def st_balance_refill_sum(msg: types.Message, state: FSMContext) -> None:
    await enter_balance_sum_text(msg, state)


async def st_balance_confirm_sum(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(await confirm_balance_text(state), reply_markup=main_menu())
