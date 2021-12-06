from utils.db.db_api.users import User
from utils.misc.date_utils import date_with_weekday
from utils.misc.user_utils import errors_msg
from utils.requests.users_reqests import UserRequest


async def st_lesson_history_text(user_id: int):
    user = await User.find(user_id)
    res = await UserRequest.st_lessons_history(user.get('role_id'))
    if res.get('success') is True:
        txt = ['👨‍🦳 Ось твої нещодавні заняття:\n']
        for ls in res.get('lessons'):
            txt.append('👉 заняття %s' % date_with_weekday(ls.get('created_at')))
        txt.append('\n*<i>Цей перелік містить до 10 занять, які відбулись нещодавно</i>')
    else:
        txt = [errors_msg['is-err']]

    return '\n'.join(txt)


async def st_pass_history_text(user_id: int):
    user = await User.find(user_id)
    res = await UserRequest.st_pass_history(user.get('role_id'))
    if res.get('success') is True:
        passes = res.get('passes')
        print(len(passes))
        if len(passes) > 0:
            txt = ['👨‍🦳 Заняття, пропущені тобою:\n']
            for ps in passes:
                txt.append('❌ пропуск %s' % date_with_weekday(ps.get('created_at')))
            txt.append('\n*<i>Цей перелік вміщає до 10 нещодавніх пропусків</i>')
        else:
            txt = ['🎉 На даний час в тебе немає пропусків.\nТак тримати! 👍']
    else:
        txt = [errors_msg['is-err']]

    return '\n'.join(txt)
