from aiogram.utils.callback_data import CallbackData


def tutor_schedule_callback(val):
    callback = CallbackData('tutorschedule', 'shift')
    if val is None:
        return callback.filter()
    else:
        return callback.new(shift=val)

