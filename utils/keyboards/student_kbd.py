from aiogram import types

from utils.misc.menu_utils import menu_str


def st_balance_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(types.KeyboardButton(text=menu_str['refill-balance']))
    k.add(types.KeyboardButton(text=menu_str['main-menu']))
    return k


def st_balance_cancel():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(types.KeyboardButton(text=menu_str['refill-balance-cancel']))
    return k


def st_balance_confirm():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(
        types.KeyboardButton(text=menu_str['refill-balance-cancel']),
        types.KeyboardButton(text=menu_str['refill-balance-confirm'])
    )
    return k


def st_schedule_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(
        types.KeyboardButton(text=menu_str['student-lessons-history']),
        types.KeyboardButton(text=menu_str['student-pass-history'])
    )
    k.add(types.KeyboardButton(text=menu_str['main-menu']))
    return k


def st_zoom_url_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(
        types.KeyboardButton(text=menu_str['student-schedule']),
        types.KeyboardButton(text=menu_str['refill-balance'])
    )
    k.add(types.KeyboardButton(text=menu_str['main-menu']))
    return k


def st_lesson_history_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(
        types.KeyboardButton(text=menu_str['student-schedule']),
        types.KeyboardButton(text=menu_str['student-pass-history'])
    )
    k.add(types.KeyboardButton(text=menu_str['main-menu']))
    return k


def st_pass_history_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(
        types.KeyboardButton(text=menu_str['student-schedule']),
        types.KeyboardButton(text=menu_str['student-lessons-history'])
    )
    k.add(types.KeyboardButton(text=menu_str['main-menu']))
    return k
