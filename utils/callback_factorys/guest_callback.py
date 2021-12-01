from aiogram.utils.callback_data import CallbackData


def get_order_callback(price_id, cost):
    callback = CallbackData('order', 'id', 'cost')
    if price_id is None:
        return callback.filter()
    else:
        return callback.new(id=price_id, cost=cost)

