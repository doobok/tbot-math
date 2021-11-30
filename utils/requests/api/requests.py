import json

import requests

from data import config
from utils.db.redis.consts import data_pool


class ExternalReq:
    @staticmethod
    async def make_request(
            url: str,
            data: dict = None,
    ):
        root_url = config.api_host.get('url')
        api_prefix = config.api_host.get('api_prefix')
        uri = f'{root_url}{api_prefix}/{url}'
        print(uri)
        token = await ExternalReq._get_token()
        headers = {'Authorization': token}
        res = requests.get(uri, params=data, headers=headers)
        if res.status_code == 200:
            try:
                res = res.json()
            except json.decoder.JSONDecodeError:
                res = False
                await ExternalReq._renew_token()
            return res
        else:
            return False

    @staticmethod
    async def _get_token():
        token = await data_pool.get('api-token', encoding='utf-8')
        if token is None:
            token = await ExternalReq._renew_token()
        return f'Bearer {token}'
    
    @staticmethod
    async def _renew_token():
        root_url = config.api_host.get('url')
        uri = f'{root_url}/oauth/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': config.api_host.get('client_id'),
            'client_secret': config.api_host.get('client_secret'),
        }
        res = requests.post(uri, data=data)
        if res.status_code == 200:
            result = res.json()
            await data_pool.set(key='api-token', value=result.get('access_token'), expire=result.get('expires_in'))
            return await data_pool.get('api-token', encoding='utf-8')
         
    