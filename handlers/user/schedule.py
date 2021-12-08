from aiogram import types

from utils.keyboards.student_kbd import st_lesson_history_menu, st_pass_history_menu, st_schedule_menu
from utils.letterings.schedule_lett import st_lesson_history_text, st_pass_history_text, st_schedule_text


async def st_schedule(msg: types.Message) -> None:
    await msg.answer(await st_schedule_text(msg.from_user.id), reply_markup=st_schedule_menu())


async def st_lesson_history(msg: types.Message) -> None:
    await msg.answer(await st_lesson_history_text(msg.from_user.id), reply_markup=st_lesson_history_menu())


async def st_pass_history(msg: types.Message) -> None:
    await msg.answer(await st_pass_history_text(msg.from_user.id), reply_markup=st_pass_history_menu())
