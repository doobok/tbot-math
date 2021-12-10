import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import api_host
from states.user import BalanceRefill
from utils.db.db_api.users import User
from utils.keyboards.student_kbd import st_balance_confirm, st_balance_cancel
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
    await state.reset_state(with_data=False)
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


async def enter_balance_text(state: FSMContext):
    await BalanceRefill.enter_sum.set()
    txt = ['👨‍🦳 На яку суму ти бажаєш поповнити свій баланс?']
    return '\n'.join(txt)


async def enter_balance_sum_text(msg: types.Message, state: FSMContext):
    cost = ''.join(re.findall(r'\d', msg.text))
    keyboard = st_balance_cancel()
    if len(cost) < 1:
        txt = '👨‍🦳 Введи число, будь-ласка'
    else:
        cost = int(cost)
        if cost < 200:
            txt = errors_msg['cost-more']
        elif cost > 20000:
            txt = errors_msg['cost-less']
        else:
            txt = f'👨‍🦳 Поповнити баланс на <b>{cost} грн</b>?'
            keyboard = st_balance_confirm()
            await state.update_data(cost=cost)
            await BalanceRefill.next()
    await msg.answer(txt, reply_markup=keyboard)


async def confirm_balance_text(state: FSMContext):
    data = await state.get_data()
    cost = data.get('cost')
    link = '%s/refill-bot?role_id=%s&sum=%s&phone=%s' \
           % (api_host['url'], data.get('role_id'), cost, data.get('phone'))
    txt = [f'👨‍🦳 Для того, щоб поповнити рахунок на <b>{cost} грн.</b>, потрібно перейти за посиланням 👇\n',
           f'{link}',
           '\nта дотримуючись підказок здійснити платіж.\n']
    await state.reset_state(with_data=False)
    return '\n'.join(txt)
