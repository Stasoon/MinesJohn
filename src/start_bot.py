from aiogram import executor

from src.middlewares.throttling import setup_middleware
from src.handlers import register_all_handlers
from src.filters import register_all_filters
from src.database import register_models
from src.create_bot import dp, bot
from src.utils import logger
from config import Config


async def on_startup(_):
    # Регистрация троттлинга
    setup_middleware(dp)

    # Регистрация фильтров
    register_all_filters(dp)

    # Регистрация хэндлеров
    register_all_handlers(dp)

    # Регистрация моделей базы данных
    register_models()

    logger.info('Бот запущен!')


async def on_shutdown(_):
    await (await bot.get_session()).close()


def start_bot():
    try:
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
    except Exception as e:
        logger.error(e)
