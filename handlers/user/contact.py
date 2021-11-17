from aiogram import types

from data import config

from utils.db.db_api.chats import Chats
from utils.db.redis.consts import data_pool
from utils.requests.api.requests import ExternalReq
from utils.requests.users_reqests import UserRequest


async def bot_contact(msg: types.Message) -> None:
    print(msg.contact.phone_number)
    if msg.from_user.id == msg.contact.user_id:
        print('is you contact')
        # await MyRedis.set_token('2834782379')

        # serv = BaseRedis.connect
        # serv.set

        await data_pool.set(key='test2', value=12)
        print(await data_pool.get('test2', encoding='utf-8'))

        # red = await MyRedis.set_val('0')
        # print(red)

        endpoint = 'http://math.cam/api/v2/auth-bot-user'
        # endpoint = 'http://math.cam/oauth/token'
        data = {
            'phone': 380686778864
            # 'grant_type': 'client_credentials',
            # 'client_id': config.api_host['client_id'],
            # 'client_secret': config.api_host['client_secret']
        }
        # headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}

        r = await UserRequest.get_role(380686778864)
        print(r)

        # print(requests.post(endpoint, data=data).json())
        # print(requests.post(endpoint, data=data, headers=headers).json())

        # r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

        if await Chats.is_new(msg):
            await Chats.register(msg)
            print('its new user')
        else:
            print('its user found')
    else:
        await msg.answer(f'Буде круто коли ти відправиш власний номер телефону 😜')

    await msg.answer(f'Дякуємо за контакт, {msg.from_user.first_name}!')

