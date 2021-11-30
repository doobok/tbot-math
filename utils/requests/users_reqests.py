from .api.requests import ExternalReq


class UserRequest(ExternalReq):
    @staticmethod
    async def get_role(phone: int):
        url = 'auth-bot-user'
        data = {'phone': phone}
        r = await UserRequest.make_request(url, data)
        return r

    @staticmethod
    async def get_prices():
        url = 'tariffs'
        return await UserRequest.make_request(url)
