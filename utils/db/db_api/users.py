from aiogram import types

from .storages import MysqlConnection


class User(MysqlConnection):
    @staticmethod
    async def is_new(msg: types.Message) -> bool:
        sql = 'SELECT `id` FROM `users` WHERE `external_id` = %s'
        params = (msg.contact.user_id,)
        r = await User._make_request(sql, params, fetch=True)
        return not bool(r)

    @staticmethod
    async def register(msg: types.Message, user):
        sql = 'INSERT INTO `users` (`first_name`, `external_id`, `phone`, `last_name`, `role`, `role_id`) ' \
              'VALUES (%s, %s, %s, %s, %s, %s)'
        params = (msg.from_user.first_name, msg.contact.user_id, msg.contact.phone_number, msg.from_user.last_name,
                  user['role'], user['role_id'])
        await User._make_request(sql, params)

    @staticmethod
    async def find(user_id: int):
        sql = 'SELECT * FROM `users` WHERE `external_id` = %s'
        params = (user_id,)
        return await User._make_request(sql, params, fetch=True)

    @staticmethod
    async def update(msg: types.Message, user):
        sql = 'SELECT * FROM `users` WHERE `external_id` = %s'
        params = (msg.contact.user_id,)
        db_user = await User._make_request(sql, params, fetch=True)
        if db_user.get('role', False) != user['role']:
            sql = 'UPDATE `users` SET `first_name` = %s, `phone` = %s, `last_name` = %s, `role` = %s, `role_id` = %s ' \
                  'WHERE `id`= %s'
            params = (msg.from_user.first_name, msg.contact.phone_number, msg.from_user.last_name,
                      user['role'], user['role_id'], db_user.get('id', False))
            await User._make_request(sql, params)
            return 'renew'
        else:
            return False

