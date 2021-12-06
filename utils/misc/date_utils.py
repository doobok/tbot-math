import datetime


def date_with_weekday(date):
    d = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    y = d.year
    m = d.month
    n = d.day
    w = week_days[d.isoweekday()]
    return f'{w} {n}-{m}-{y}'


def date_hour_minutes(date):
    d = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    h = d.hour
    m = d.minute
    return f'{h}:{m}'


week_days = {
    1: 'Понеділок',
    2: 'Вівторок',
    3: 'Середа',
    4: 'Четвер',
    5: 'Пʼятниця',
    6: 'Субота',
    0: 'Неділя',
}
