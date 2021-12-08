from .api.requests import ExternalReq
from ..db.db_api.users import User


class UserRequest(ExternalReq):
    @staticmethod
    async def get_role(phone: int):
        url = 'auth-bot-user'
        data = {'phone': phone}
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def get_prices():
        url = 'tariffs'
        return await UserRequest.make_request(url)

    @staticmethod
    async def new_oder(price_id: int, cost: int, user_id: int):
        user = await User.find(user_id)
        url = 'new-order'
        data = {
            'name': user.get('first_name'),
            'phone': user.get('phone'),
            'price_id': price_id,
            'cost': cost,
        }
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def get_balance(role: str, role_id: int):
        url = 'get-balance'
        data = {'role': role, 'role_id': role_id}
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def get_tutor_zoom(role_id: int):
        url = 'tutor-zoom'
        data = {'role_id': role_id}
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def st_schedule(role_id: int):
        url = 'student-schedule'
        data = {'role_id': role_id}
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def st_lessons_history(role_id: int):
        url = 'student-lessons-history'
        data = {'role_id': role_id}
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def st_pass_history(role_id: int):
        url = 'student-pass-history'
        data = {'role_id': role_id}
        return await UserRequest.make_request(url, data)

    @staticmethod
    async def st_zoom_url(role_id: int, lesson_id: int):
        url = 'student-zoom-url'
        data = {'role_id': role_id, 'lesson_id': lesson_id}
        return await UserRequest.make_request(url, data)

