import datetime


# дата з іменем дня тижня без годин (сирі дані із бд)
def date_with_weekday(date):
    d = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    y = d.year
    m = d.month
    n = d.day
    w = week_days[d.isoweekday()]
    return f'{w} {n}-{m}-{y}'


# дата з іменем дня тижня без годин (yyyy-mm-dd)
def date_weekday(date):
    d = datetime.datetime.strptime(date, '%Y-%m-%d')
    y = d.year
    m = d.month
    n = d.day
    w = week_days[d.isoweekday()]
    return f'{w} {n}-{m}-{y}'


# години і хвилини (yyyy-mm-dd HH:MM:SS)
def date_hour(date):
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    h = d.hour
    m = d.minute
    if m < 10:
        m = '0' + str(m)
    return f'{h}:{m}'


week_days = {
    1: 'Понеділок',
    2: 'Вівторок',
    3: 'Середа',
    4: 'Четвер',
    5: 'Пʼятниця',
    6: 'Субота',
    7: 'Неділя',
}
