from aiogram import types

from utils.db.db_api.users import User
from utils.misc.user_utils import user_roles, user_possibilities
from utils.requests.users_reqests import UserRequest

# опрацювання контактів, реєструє користувачів та вносить зміни в існуючі записи


async def bot_contact(msg: types.Message) -> None:
    if msg.from_user.id == msg.contact.user_id:
        user = await UserRequest.get_role(int(msg.contact.phone_number))
        role = user_roles[user['role']]
        func = user_possibilities[user['role']]

        if await User.is_new(msg):
            await User.register(msg, user)
            inf = ['Тебе успішно зареєстровано\n']
        else:
            if await User.update(msg, user) == 'renew':
                inf = ['Реєстраційний запис оновлено\n']
            else:
                inf = ['Роль користувача залишилась без змін\n']
        txt = [
            f'Привіт, {msg.from_user.first_name}!\n',
            '\n'.join(inf),
            f'Твоя поточна роль в системі: <b>{role}</b>\n'
            f'Для тебе доступні наступні команди: \n\n {func} \n\n'
            f'*якщо роль не відповідає дійсності, звʼяжись з нами, ми спробуємо допомогти'
        ]
    else:
        txt = [
            'Буде круто коли ти відправиш мені власний номер телефону 😜'
        ]

    await msg.answer('\n'.join(txt))

