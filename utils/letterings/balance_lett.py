from aiogram.dispatcher import FSMContext

from utils.db.db_api.users import User
from utils.misc.user_utils import errors_msg
from utils.requests.users_reqests import UserRequest


async def tutor_balance_text(user_id: int, state: FSMContext):
    user = await User.find(user_id, state)
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


async def student_balance_text(user_id: int, state: FSMContext):
    user = await User.find(user_id, state)
    res = await UserRequest.get_balance(user.get('role'), user.get('role_id'))
    if res.get('success') is True:
        balance = res.get('balance')
        if balance > 500:
            info = '😉 На твоєму балансі достатньо коштів, Приємного навчання!'
        elif balance > 0:
            info = '😐 Кошти закінчуються, рекомендую поповнити рахунок для уникнення збоїв при роботі з системою'
        else:
            info = '🥶 Баланс спустошено! Можливі обмеження в функціоналі! Поповніть, будь-ласка, рахунок'
        txt = [
            '👨‍🦳 На твоєму балансі ',
            f'💶 <b>{balance} грн.*</b>',
            f'{info}',
            '<i>*списання коштів з балансу відбувається раз на добу</i>'
        ]
    else:
        txt = [errors_msg['is-err']]

    return '\n\n'.join(txt)
