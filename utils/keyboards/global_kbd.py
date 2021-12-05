from aiogram import types

from utils.misc.menu_utils import menu_str


def send_phone():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    return k.add(types.KeyboardButton(text=menu_str['send-phone'], request_contact=True))


def main_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    return k.add(types.KeyboardButton(text=menu_str['main-menu']))


def remove_kbd():
    return types.ReplyKeyboardRemove()


def tutor_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(types.KeyboardButton(text=menu_str['tutor-schedule']))
    k.add(types.KeyboardButton(text=menu_str['tutor-balance']))
    k.add(types.KeyboardButton(text=menu_str['tutor-zoom']))
    return k


def student_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(types.KeyboardButton(text=menu_str['student-schedule']))
    k.add(
        types.KeyboardButton(text=menu_str['student-lessons-history']),
        types.KeyboardButton(text=menu_str['student-pass-history'])
    )
    k.add(types.KeyboardButton(text=menu_str['student-balance']))

    return k
