from aiogram import types

from .storages import MysqlConnection


class Chats(MysqlConnection):
    @staticmethod
    async def is_new(msg: types.Message) -> bool:
        sql = 'SELECT `id` FROM `users` WHERE `phone` = %s'
        params = (msg.contact.phone_number,)
        r = await Chats._make_request(sql, params, fetch=True)
        return not bool(r)

    @staticmethod
    async def register(msg: types.Message):
        sql = 'INSERT INTO `users` (`first_name`, `external_id`, `phone`, `last_name`) VALUES (%s, %s, %s, %s)'
        params = (msg.from_user.first_name, msg.contact.user_id, msg.contact.phone_number, msg.from_user.last_name)
        await Chats._make_request(sql, params)
