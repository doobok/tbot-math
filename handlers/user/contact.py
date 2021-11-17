from aiogram import types

from utils.db.db_api.chats import Chats
from utils.requests.users_reqests import UserRequest


async def bot_contact(msg: types.Message) -> None:
    if msg.from_user.id == msg.contact.user_id:

        r = await UserRequest.get_role(msg.contact.phone_number)
        print(r)

        if await Chats.is_new(msg):
            await Chats.register(msg)
            print('its new user')
        else:
            print('its user found')
    else:
        await msg.answer(f'Буде круто коли ти відправиш власний номер телефону 😜')

    await msg.answer(f'Дякуємо за контакт, {msg.from_user.first_name}!')

