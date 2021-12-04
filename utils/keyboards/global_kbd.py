from aiogram import types


def send_phone():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    return k.add(types.KeyboardButton(text="📞 Надіслати номер телефону", request_contact=True))


def tutor_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(types.KeyboardButton(text="Показати розклад"))
    k.add(types.KeyboardButton(text="Перевірити баланс"))
    return k


def student_menu():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k.add(
        types.KeyboardButton(text="Показати розклад"),
        types.KeyboardButton(text="Баланс")
        )
    return k
