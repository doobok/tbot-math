from data import config

from utils.db.redis.consts import BaseRedis


async def troll():
    host = config.myredis['address']
    password = config.myredis['password']
    redis = BaseRedis(host=host, db=1, password=password)
    db = await redis.redis()
    # await db.set('keysss', 'troll')