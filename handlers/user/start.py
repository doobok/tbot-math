from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.db.db_api.users import User
from utils.keyboards.global_kbd import send_phone, tutor_menu, student_menu
from utils.letterings.intro_lett import first_text, start_guest_text, start_tutor_text, start_student_text
from utils.misc.menu_utils import menu_str
from utils.misc.stickers import my_stickers


async def bot_start(msg: types.Message, state: FSMContext):
    u = await User.find(msg.from_user.id, state)
    if u is None:
        await msg.answer(first_text(msg.from_user.full_name), reply_markup=send_phone())
    else:
        if u.get('role') == 'student':
            await msg.answer_sticker(my_stickers['hello'])
            await msg.answer(start_student_text(u.get('first_name')), reply_markup=student_menu())
        elif u.get('role') == 'tutor':
            await msg.answer(start_tutor_text(u.get('first_name')), reply_markup=tutor_menu())
        else:
            await msg.answer(start_guest_text(u), reply_markup=send_phone())


async def main_menu(msg: types.Message, state: FSMContext):
    u = await User.find(msg.from_user.id, state)
    if u.get('role') == 'student':
        await msg.answer(menu_str['main-menu'], reply_markup=student_menu())
        await msg.delete()
    elif u.get('role') == 'tutor':
        await msg.answer(menu_str['main-menu'], reply_markup=tutor_menu())
        await msg.delete()
