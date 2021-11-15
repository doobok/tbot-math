import aioredis

from data import config


class MyRedis:
    @staticmethod
    async def set_token(val: str):
        # connection = await aioredis.create_redis_pool(**config.myredis, db=1)
        # await connection.set(key='test', value='Hello world!')

        db = aioredis.from_url('redis://127.0.0.1:6379/1', decode_responses=True)

        # redis_conn = aioredis.Redis(connection_pool=data_pool)

        # r = await aioredis.Redis.set(self, key='test', value='hello world!')

        # r = await BaseRedis.redis.__setattr__('test', 'hello world!')
        # ('seter': 1111)

        # sql = 'SELECT `id` FROM `users` WHERE `phone` = %s'
        # r = await Chats._make_request(sql, params, fetch=True)
        return not bool(True)
