from utils.db.db_api.users import User
from utils.misc.user_utils import errors_msg
from utils.requests.users_reqests import UserRequest


async def tutor_balance_text(user_id: int):
    user = await User.find(user_id)
    res = await UserRequest.get_balance(user.get('role'), user.get('role_id'))
    if res.get('success') is True:
        balance = res.get('balance')
        txt = [
            '👨‍🦳 На Вашому балансі ',
            f'💶 <b>{balance} грн.*</b>',
            'належних до відшкодування',
            '<i>*відшкодування нараховуються раз на добу під кінець доби</i>'
        ]
    else:
        txt = [errors_msg['is-err']]

    return '\n\n'.join(txt)


async def tutor_zoom_text(user_id: int):
    user = await User.find(user_id)
    res = await UserRequest.get_tutor_zoom(user.get('role_id'))
    if res:
        txt = [
            '👨‍🦳 ось Ваші дані для аутентифікації в Zoom:\n\n'
            'email: <code>%s</code>\n'
            'пароль: <code>%s</code>\n\n'
            'Для підключення до онлайн занять у Вас також має бути встановлений клієнт Zoom, який можна завантажити '
            'за посиланням 👉 https://zoom.us/download\n\n'
            '<i>* при зміні пароля на порталі Zoom вказаний в цьому повідомленні пароль втрачає свою дію</i>' %
            (res.get('zoom_email'), res.get('zoom_password'))
        ]
    else:
        txt = [errors_msg['is-err']]

    return '\n\n'.join(txt)

