import asyncio
import random

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from src.database.user import create_user_if_not_exist, set_user_1win_id, get_user_1win_id
from src.utils import send_typing_action
from src.misc import UserDataInputting
from .messages import Messages
from .kb import Keyboards
from config import CODE_WORD


async def send_before_start(to_message):
    await to_message.answer_photo(
        caption=Messages.get_before_game_start(),
        reply_markup=Keyboards.get_first_signal_markup(),
        photo=Messages.get_before_game_start_photo()
    )


# region Handlers

async def __handle_start_command(message: Message) -> None:
    await send_typing_action(message)

    create_user_if_not_exist(
        telegram_id=message.from_id,
        name=message.from_user.username or message.from_user.full_name,
        reflink=message.get_full_command()[1]
    )

    await message.answer_photo(
        photo=Messages.get_welcome_photo_url(),
        caption=Messages.get_welcome(message.from_user.first_name),
        reply_markup=Keyboards.get_welcome_menu()
    )


async def __handle_start_callback(callback: CallbackQuery, state: FSMContext):
    await send_typing_action(callback.message)
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer_photo(
        caption=Messages.get_after_welcome_explanation(),
        photo=Messages.get_after_welcome_explanation_photo(),
        reply_markup=Keyboards.get_after_welcome_menu()
    )
    # await callback.message.answer(Messages.ask_for_1win_id())
    # await state.set_state(UserDataInputting.wait_for_id.state)


# async def __handle_user_id_message(message: Message, state: FSMContext):
#     await send_typing_action(message)
#
#     if not message.text.isdigit():
#         await message.answer(Messages.get_1win_id_have_forbidden_symbols())
#         return
#     if len(message.text) not in (8, 9):
#         await message.answer(Messages.get_1win_id_incorrect_length())
#         return
#
#     set_user_1win_id(message.from_user.id, message.text)
#     await message.answer(Messages.ask_for_code_word())
#     await state.set_state(UserDataInputting.wait_for_password.state)


async def __handle_after_welcome_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(text=Messages.ask_for_code_word())
    await state.set_state(UserDataInputting.wait_for_password.state)


async def __handle_user_password_message(message: Message, state: FSMContext):
    await send_typing_action(message)
    if message.text.lower() != CODE_WORD.lower():
        await message.answer(Messages.get_code_word_incorrect())
        return

    await send_before_start(to_message=message)
    await state.finish()


async def __handle_next_signal_callback(callback: CallbackQuery):
    # Удаляем сообщение
    await send_typing_action(callback.message)
    await callback.answer(text=Messages.get_loading())
    await callback.message.edit_reply_markup(reply_markup=None)

    # Делаем видимость вычислений
    delay_seconds = random.randint(2, 5)
    await asyncio.sleep(delay_seconds)

    new_photo = Messages.get_random_signal()

    await callback.message.answer_photo(photo=new_photo, reply_markup=Keyboards.get_next_signal_markup())


# endregion


def register_user_handlers(dp: Dispatcher) -> None:
    # обработка команды /start
    dp.register_message_handler(__handle_start_command, CommandStart())

    # обработка кнопок приветственного меню
    dp.register_callback_query_handler(__handle_start_callback, text='welcome_menu', state=None)
    dp.register_callback_query_handler(__handle_after_welcome_callback, text='after_welcome_menu', state=None)
    # dp.register_message_handler(__handle_user_id_message, state=UserDataInputting.wait_for_id)
    dp.register_message_handler(__handle_user_password_message, state=UserDataInputting.wait_for_password)

    # обработка нажатия на Следующий сигнал
    dp.register_callback_query_handler(__handle_next_signal_callback, text='next_signal')
