user_roles = {
    'student': 'Учень',
    'tutor': 'Тьютор',
    'guest': 'Гість',
}

user_possibilities = {
    'student': f'- розклад занять /shedule\n'
               f'- історія відвіданих занять /history\n'
               f'- історія пропусків /passes\n'
               f'- баланс /balance\n'
               f'- поповнити баланс /refill_balance',

    'tutor': f'- розклад занять /shedule\n'
             f'- баланс /balance',

    'guest': f'- знайомство з платформою /info\n'
             f'- ціни на послуги /pricing',
}

registration_status = {
    'new': '✅ Тебе успішно зареєстровано',
    'updated': '🔄 Реєстраційний запис оновлено',
    'no-updated': '🧐 Роль користувача залишилась без змін'
}

errors_msg = {
    'is-err': '🤷 Виникла помилка, будь-ласка, повторіть спробу пізніше',
    'no-balance-for-zoom': '⚠️ Коштів на балансі не достатньо для оплати заняття!. \n'
                           'Щоб отримати посилання для доступу до заняття, поповни свій рахунок!',
    'zoom-url-time-limit': '⚠️ Посилання доступне за 30хв до початку занняття та дійсне до його закінчення.\n\n'
                           '<b>Чому я бачу це повідомлення?</b> \n\n'
                           'Можливих варіантів кілька:\n'
                           '1. Ти занадто рано намагаєшся отримати посилання, спробуй повторити не раніше ніж '
                           'за 30 хв. до початку заняття.\n'
                           '2. Заняття вже закінчилось, неможливо отримати посилання на завершені заняття.',
    'no-found-zoom-url': '⚠️ Отакої!\nЯ не зміг знайти посилання, схоже що його не існує 😨',

}
