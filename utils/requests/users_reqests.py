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
