import requests

from data import config


class ExternalReq:
    @staticmethod
    async def make_request(
            url: str,
            data: dict = None,
    ):
        root_url = config.api_host.get('url')
        uri = f'{root_url}/{url}'
        print(uri)
        token = await ExternalReq._get_token()
        headers = {'Authorization': token}
        return requests.get(uri, data=data, headers=headers).json()

    @staticmethod
    async def _get_token(

    ):
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiM2M1YmI5NDhmZTMxMTFiZm' \
               'U1ZjlhMDY3YTcx' \
               'M2RkYmM3OTg3ZDhiNmJkZWQxYWUzYWU4YWM5YTg0ZmFhOTQxZWJiNzU2OWFlZGJlMDVhNzEiLCJpYXQiOjE2MzY2NjMxNjAsI' \
               'm5iZiI6MTYzNjY2MzE2MCwiZXhwIjoxNjY4MTk5MTYwLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.Hs6MIG5al0KSSZJjUJqVqy' \
               'oC8UlZrn1LcYO8e4VUZBZPTNjKwgJzHwjLe-hN-MpyqVQtClefW7hfLf_mbzuPkQKTkjAFZuaPhPppUlrt4HYdtj-YxSUDiy' \
               'nbkj3f2D3md0Ycb8_-Bdtbcvs4vgITXm3zGpuMkFtA67iT5qTYdG_ZHdU3yN_6NsT3qByuTsBXfIHwX-SkxoLRSRnWbGpDQc26' \
               'vsg3PX0SW8tmR56iMosbAZ-HQvPlnW2sEjGU3Sz_YORp6bJ45oUymiVdrd_2QBJCI4yFcU9ep2CGnSiq51Xr9MkS318-zxNXkZf' \
               'lADBVRGukkTGjzRpZg1ZenKPUZlYuSaTuzS9YgUCnY6w1NlguF2eZorwdBgPbIJTuK_8dEi3TsIQBEMwyGPNvOVtHiVRSsD7bd' \
               'JLQ39W5c-2o-ZMLsVpWwOykaCkF2m2aJ6EloN843aX6ORKoQj0RL9KFLw09UVaCuQHLS6ga3fc4CddQnJhMUESMVnF3GiDPDSr' \
               'VZbkmbsBejiNRjtQ4UgqpW6pvYVJiEnTDK9xOV2grPDBgE2UwYhcAmhxorq5KDp4MhIlgVVx3fzadZVkNGMf95nvKPJOrJBapC' \
               'X1tRrV_ioc-yIIBUkdreNQdXBkWXgWxzqyfD3mwKqMfip4mFsQ7fZFCR1bMi0HpTyMEYrncqjs'
        return f'Bearer {token}'
