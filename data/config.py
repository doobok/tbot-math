import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = os.getenv('BASE_URL')  # Webhook domain
WEBHOOK_PATH = f'/tg/webhooks/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

LOGS_BASE_PATH = str(Path(__file__).parent.parent / 'logs')

admins = []

ip = {
    'db':    os.getenv('LOCAL_IP'),
    'redis': os.getenv('LOCAL_IP'),
    'port': os.getenv('WEBAPP_PORT')
}

mysql_info = {
    'host':     ip['db'],
    'user':     os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'db':       os.getenv('DB_NAME'),
    'maxsize':  5,
    'port':     int(os.getenv('DB_PORT')),
}

redis = {
    'host':     ip['redis'],
    'password': os.getenv('REDIS_PASSWORD')
}
myredis = {
    'address':  'redis://' + ip['redis'],
    'password': os.getenv('REDIS_PASSWORD')
}

api_host = {
    'url': os.getenv('SERV_URL'),
    'api_prefix': '/api/v2',
    'client_id': os.getenv('SERV_CLIENT_ID'),
    'client_secret': os.getenv('SERV_CLIENT_SECRET')
}
