from aiogram import types

from utils.keyboards.global_kbd import main_menu
from utils.keyboards.student_kbd import st_lesson_history_menu, st_pass_history_menu, st_schedule_menu, st_zoom_url_menu
from utils.letterings.schedule_lett import st_lesson_history_text, st_pass_history_text, st_schedule_text, \
    st_zoom_url_text, tutor_zoom_text


async def st_schedule(msg: types.Message) -> None:
    await msg.answer(await st_schedule_text(msg.from_user.id), reply_markup=st_schedule_menu())


async def st_zoom_url(msg: types.Message, regexp_command=None) -> None:
    lesson_id = regexp_command.group(1)
    await msg.answer(await st_zoom_url_text(msg.from_user.id, lesson_id), reply_markup=st_zoom_url_menu(),
                     disable_web_page_preview=True)


async def st_lesson_history(msg: types.Message) -> None:
    await msg.answer(await st_lesson_history_text(msg.from_user.id), reply_markup=st_lesson_history_menu())


async def st_pass_history(msg: types.Message) -> None:
    await msg.answer(await st_pass_history_text(msg.from_user.id), reply_markup=st_pass_history_menu())


async def tutor_zoom(msg: types.Message) -> None:
    await msg.answer(await tutor_zoom_text(msg.from_user.id), reply_markup=main_menu(), disable_web_page_preview=True)
