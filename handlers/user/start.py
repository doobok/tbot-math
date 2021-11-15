from aiogram import types


async def bot_start(msg: types.Message):
    print(msg.from_user)
    text = f'Привіт, {msg.from_user.full_name}! Мене звати Платон, я буду твоїм віртуальним асистентом, ' \
           f'моє основне призначення  - налагодження комунікації між учнями, репетиторами та освітнім центром. ' \
           f'Для початку давай спробуємо знайти твій номер телефону в базі освітнього центру, ' \
           f'так я зможу зрозуміти твою роль та наділити тебе відповідними повноваженнями. \n ' \
           f'Для цього надішли мені його використавши відповідну кнопку.'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="📞 Надіслати номер телефону", request_contact=True))
    await msg.answer(text, reply_markup=keyboard)
