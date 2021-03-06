from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.db.db_api.users import User
from utils.misc.stickers import my_stickers
from utils.requests.users_reqests import UserRequest


async def info_text(msg: types.Message, state: FSMContext):
    txt = [
        'Tutor-Math ❤ - це навчальний репетиторський центр, який допомагає учням поглибити знання з предметів '
        'шкільного циклу, підготуватися до контрольних, творчих робіт, іспитів та олімпіад. Ми працюємо як в '
        'онлайні так і офлайн, перелік центрів на нашому сайті https://tutor-math.com.ua \n',
        'Цей бот виконує роль цифрового асистента нашого освытнього центру, '
        'до його "умінь" можна віднести роботу з розкладом, балансом, '
        'статистикою та іншими корисностями\n',
        'Ми намагалися зробити максимально зручний інструмент, який був би завжди під рукою.',
    ]
    user = await User.find(msg.from_user.id, state)
    if user is None or user.get('role_id', 0) < 1:
        txt.append('\nСпробуй сам та переконайся!\n'
                   'Для початку потрібно стати учнем нашого центру, тарифи тут 👉 /pricing')
    await msg.answer('\n'.join(txt), disable_web_page_preview=True)


async def info_prices_text(msg: types.Message, state: FSMContext):
    user = await User.find(msg.from_user.id, state)
    if user is None or user.get('role_id', 0) < 1:
        prices = await UserRequest.get_prices()
        txt = ['👩‍🏫 <b>Абонементи / пакети послуг</b>',
               'Заняття в нашому освітньому центрі, орієнтовані на результат. Саме тому ми пропонуємо пакети послуг, '
               'основний принцип яких: більше займаєшся - платиш менше\n',
               'Обери зручний пакет послуг та натисни на команду для замовлення',
               'Наразі для тебе доступні наступні пакети послуг:\n',
               ]
        for p in prices:
            txt.append('🎁 <b>%s %s</b>, кількість занять <b>%s</b> всього <b>%s</b> грн. вартість одного заняття '
                       '<b>%s</b> грн. \n замовити 👉 /price_%s\n' %
                       (p.get('name'), p.get('group'), p.get('count'), p.get('price') * p.get('count'), p.get('price'),
                        p.get('id')))
        txt.append('Окрім того ти можеш скористатися пробним заняттям, спеціальна ціна чекає на тебе за посиланням '
                   '👉 https://tutor-math.com.ua/trial-lesson')
    else:
        await msg.answer_sticker(my_stickers['attention'])
        txt = ['👨‍🦳☝️ Ця сторінка доступна для нових користувачів, які не зареєстровані в системі']
    await msg.answer('\n'.join(txt), disable_web_page_preview=True)


def get_price_text(p: dict):
    txt = [
        '🎁 Ти дійсно бажаєш замовити пакет послуг <b>%s %s</b>\n'
        'загальна вартість <b>%s грн.</b> \n'
        'за <b>%s занять</b>\n'
        '(%s грн./заняття)?\n\n'
        'Для підтвердження натисни <b>"Замовити"</b>' %
        (p.get('name'), p.get('group'), p.get('price') * p.get('count'), p.get('count'), p.get('price'))
    ]
    return '\n'.join(txt)


def get_price_success_text():
    return '✅ Замовлення прийняте!\n' \
           'Очікуй дзвінка, або відповіді менеджера 👩‍🦰\n' \
           'Вже зовсім скоро ти приєднаєшся\n' \
           'до Tutor-Math ❤️'


def get_price_err_text():
    return '❌ Виникла помилка, повторіть спробу пізніше!'


def err_get_price_text(price_id: int):
    txt = [
        f'😔 Нажаль пакета з ідентифікатором: <b>{price_id}</b> не існує, або він втратив свою актуальність.',
        '😊 Обери, будь-ласка, інший пакет послуг серед актуальних! 👉 /pricing'
    ]
    return '\n'.join(txt)
