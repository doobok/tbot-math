from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.db.db_api.users import User
from utils.keyboards.global_kbd import remove_kbd, send_phone
from utils.letterings.intro_lett import err_phone_text, bot_contact_text
from utils.requests.users_reqests import UserRequest

# опрацювання контактів, реєструє користувачів та вносить зміни в існуючі записи


async def bot_contact(msg: types.Message, state: FSMContext) -> None:
    if msg.from_user.id == msg.contact.user_id:
        user = await UserRequest.get_role(int(msg.contact.phone_number), int(msg.from_user.id))
        if await User.is_new(msg):
            await User.register(msg, user)
            inf = 'new'
        else:
            if await User.update(msg, user, state) == 'renew':
                inf = 'updated'
            else:
                inf = 'no-updated'
        txt = bot_contact_text(user, msg.from_user.first_name, inf)
        kbd = remove_kbd()
    else:
        txt = err_phone_text()
        kbd = send_phone()

    await msg.answer(txt, reply_markup=kbd)

