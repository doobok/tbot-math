from aiogram import types

from utils.callback_factorys.guest_callback import get_order_callback
from utils.requests.users_reqests import UserRequest


async def guest_info(msg: types.Message):
    txt = [
        f'Tutor-Math - це навчальний репетиторський центр, який допомагає учням поглибити знання з предметів '
        f'шкільного циклу, підготуватися до контрольних, творчих робіт, іспитів та олімпіад. Ми працюємо як в '
        f'онлайні так і офлайн, перелік центрів на нашому сайті https://tutor-math.com.ua \n\n'
        f'Цей бот виконує роль цифрового асистента нашого освытнього центру, '
        f'до його "умінь" можна віднести роботу з розкладом, балансом, '
        f'статистикою та іншими корисностями\n\n'
        f'Ми намагалися зробити максимально зручний інструмент, який був би завжди під рукою.\n'
        f'Спробуй сам та переконайся\n\n'
        f'Для початку потрібно стати учнем нашого центру, тарифи тут 👉 /pricing'
    ]
    await msg.answer('\n'.join(txt))


async def guest_pricing(msg: types.Message):
    prices = await UserRequest.get_prices()
    txt = ['👩‍🏫 <b>Абонементи / пакети послуг</b>\n'
           'Заняття в нашому освітньому центрі, орієнтовані на результат. Саме тому ми пропонуємо пакети послуг, '
           'основний принцип яких: більше займаєшся - платиш менше\n'
           'Обери зручний пакет послуг та натисни на команду для замовлення\n'
           'Наразі для тебе доступні наступні пакети послуг:\n'
    ]
    for p in prices:
        txt.append('🎁 <b>%s %s</b>, кількість занять <b>%s</b> всього <b>%s</b> грн. вартість одного заняття '
                   '<b>%s</b> грн. \n замовити 👉 /price_%s\n' %
                   (p.get('name'), p.get('group'), p.get('count'), p.get('price')*p.get('count'), p.get('price'),
                    p.get('id')))
    txt.append('\nОкрім того ти можеш скористатися пробним заняттям, спеціальна ціна чекає на тебе за посиланням '
               '👉 https://tutor-math.com.ua/trial-lesson')
    await msg.answer('\n'.join(txt))


async def guest_price(msg: types.Message, regexp_command=None):
    price_id = regexp_command.group(1)
    prices = await UserRequest.get_prices()
    p = next((x for x in prices if x['id'] == int(price_id)), False)
    if isinstance(p, dict):
        txt = [
            '🎁 Ти дійсно бажаєш замовити пакет послуг <b>%s %s</b>\n'
            'загальна вартість <b>%s грн.</b> \n'
            'за <b>%s занять</b>\n'
            '(%s грн./заняття)?\n\n'
            'Для підтвердження натисни <b>"Замовити"</b>' %
            (p.get('name'), p.get('group'), p.get('price')*p.get('count'), p.get('count'), p.get('price'))
        ]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('🎁 Замовити',
                     callback_data=get_order_callback(price_id, p.get('price')*p.get('count'))))
    else:
        txt = [f'😔 Нажаль пакета з ідентифікатором: {price_id} не існує, або він втратив свою актуальність. '
               f'😊 Обери, будь-ласка, інший пакет послуг серед актуальних! 👉 /pricing']
        keyboard = None
    await msg.answer('\n'.join(txt), reply_markup=keyboard)


async def ordered_price(query: types.CallbackQuery, callback_data: dict):
    price_id = int(callback_data['id'])
    cost = int(callback_data['cost'])
    user_id = query.message.chat.id
    r = await UserRequest.new_oder(price_id, cost, user_id)
    if r.get('success'):
        await query.answer('✅ Замовлення прийняте!')
        await query.message.edit_text('✅ Замовлення прийняте! \nОчікуй дзвінка, або відповіді менеджера 👩‍🦰\n'
                                      'Вже зовсім скоро ти приєднаєшся \nдо Tutor-Math ❤️')
    else:
        await query.answer('❌ Виникла помилка, повторіть спробу пізніше!')

