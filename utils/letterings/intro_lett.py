from utils.misc.user_utils import user_possibilities, user_roles, registration_status


def help_text():
    txt = [
        '👨‍🦳 З чого розпочати?\n',
        'ось кілька команд\n',
        '/start - Розпочати роботу',
        '/help - Отримати довідку',
        '/info - Інформація про проект'
    ]
    return '\n'.join(txt)


def first_text(name: str):
    txt = [
        f'👨‍🦳 Привіт, {name}! Мене звати Платон\n',
        'Я буду твоїм віртуальним асистентом, '
        'моє основне призначення  - налагодження комунікації між учнями, репетиторами та освітнім центром.\n',
        'Для початку давай спробуємо знайти твій номер телефону в базі освітнього центру, '
        'так я зможу зрозуміти твою роль та наділити тебе відповідними повноваженнями.\n',
        'Для цього надішли мені його використавши відповідну кнопку ⬇️'
    ]
    return '\n'.join(txt)


def start_guest_text(user: dict):
    func = user_possibilities[user['role']]
    name = user['first_name']
    txt = [
        f'👨‍🦳 Привіт, {name}!\n',
        f'Ти наш <b>гість</b> і для тебе доступні наступні команди: \n\n {func} \n',
        'також ти завжди можеш повторно відправити номер телефону, щоб перевірити свою роль в системі\n',
        'Де кнопка ти вже знаєш 😉 ⬇️'
    ]
    return '\n'.join(txt)


def start_tutor_text(name: str):
    txt = [
        f'👨‍🦳 Радий Вас бачити, {name}!',
        'З чого розпочнемо?',
    ]
    return '\n'.join(txt)


def start_student_text(name: str):
    txt = [
        f'👨‍🦳 Привіт, {name}!',
        'З чого ти бажаєш розпочати?',
    ]
    return '\n'.join(txt)


def bot_contact_text(user: dict, name, inf):
    func = user_possibilities[user['role']]
    role = user_roles[user['role']]
    status = registration_status[inf]
    txt = [
        f'👨‍🦳 Привіт, {name}!\n',
        f'{status}\n',
        f'Твоя поточна роль в системі: <b>{role}</b>\n'
        f'Для тебе доступний такий функціонал: \n\n {func} \n\n'
        'перейти в головне меню 👉 /start\n',
        '*якщо роль не відповідає дійсності, звʼяжись з нами, ми спробуємо допомогти'
    ]
    return '\n'.join(txt)


def err_phone_text():
    return 'Буде круто коли ти відправиш мені власний номер телефону 😜'
