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

    'tutor':   f'- розклад занять /shedule\n'
               f'- баланс /balance',

    'guest':   f'- знайомство з платформою /info\n'
               f'- ціни на послуги /pricing',
}

registration_status = {
    'new': '✅ Тебе успішно зареєстровано',
    'updated': '🔄 Реєстраційний запис оновлено',
    'no-updated': '🧐 Роль користувача залишилась без змін'
}
