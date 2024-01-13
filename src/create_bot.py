from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import Config


bot = Bot(token=Config.TOKEN, parse_mode='html')
Bot.set_current(bot)

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
