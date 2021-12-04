from aiogram import types

from utils.letterings.intro_lett import help_text
from utils.misc import rate_limit


@rate_limit(5, 'help')
async def bot_help(msg: types.Message):
    await msg.answer(help_text())
