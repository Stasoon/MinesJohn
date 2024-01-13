import os
from typing import Final
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


CODE_WORD = 'GGWIN76'


class Config:
    TOKEN: Final = os.getenv('BOT_TOKEN', 'Впишите токен в .env!')
    ADMIN_IDS: Final = tuple(int(i) for i in str(os.getenv('BOT_ADMIN_IDS')).split(','))

    SIGNALS_IMAGES_DIR = './resources/'

    DEBUG: Final = bool(os.getenv('DEBUG'))
