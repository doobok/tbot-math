from aiogram import types


async def bot_another(msg: types.Message):

    # print(msg)
    await msg.answer(f'Повідомлення за замовчуванням, {msg.from_user.full_name}!')
