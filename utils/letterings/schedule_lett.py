from utils.db.db_api.users import User
from utils.misc.user_utils import errors_msg
from utils.requests.users_reqests import UserRequest


async def st_lesson_history_text(user_id: int):
    user = await User.find(user_id)
    res = await UserRequest.st_lessons_history(user.get('role_id'))
    print(res)
    if res.get('success') is True:
        txt = ['👨‍🦳 Ось твої нещодавні заняття:']
        for ls in res.get('lessons'):
            txt.append('👉 заняття %s' % ls.get('created_at')[:10])
        txt.append('*<i>Цей перелік вміщає лише кілька нещодавніх занять</i>')
    else:
        txt = [errors_msg['is-err']]

    return '\n\n'.join(txt)


async def st_pass_history_text(user_id: int):
    user = await User.find(user_id)
    res = await UserRequest.st_pass_history(user.get('role_id'))
    print(res)
    if res.get('success') is True:
        txt = ['👨‍🦳 Заняття, пропущені тобою:']
        for ls in res.get('passes'):
            txt.append('👉 пропуск %s' % ls.get('created_at')[:10])
        txt.append('*<i>Цей перелік вміщає до 10 нещодавніх пропусків</i>')
    else:
        txt = [errors_msg['is-err']]

    return '\n\n'.join(txt)
