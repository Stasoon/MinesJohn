from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData


class Keyboards:
    locale_callback_data = CallbackData('locale', 'language_code')

    # region Subchecking

    check_sub_button = InlineKeyboardButton(text='❓ Проверить ❓', callback_data='checksubscription')

    @classmethod
    def get_not_subbed_markup(cls, channels_to_sub_data) -> InlineKeyboardMarkup | None:
        if len(channels_to_sub_data) == 0:
            return None

        cahnnels_markup = InlineKeyboardMarkup(row_width=1)
        [
            cahnnels_markup.add(InlineKeyboardButton(channel_data.get('title'), url=channel_data.get('url')))
            for channel_data in channels_to_sub_data
        ]
        cahnnels_markup.add(cls.check_sub_button)
        return cahnnels_markup

    # endregion

    @staticmethod
    def get_welcome_menu() -> InlineKeyboardMarkup:
        start_button = InlineKeyboardButton('ПРОДОЛЖИТЬ ✅', callback_data='welcome_menu')
        return InlineKeyboardMarkup(row_width=1).add(start_button)

    @staticmethod
    def get_after_welcome_menu() -> InlineKeyboardMarkup:
        start_button = InlineKeyboardButton('👇 ДАЛЕЕ 👇', callback_data='after_welcome_menu')
        return InlineKeyboardMarkup(row_width=1).add(start_button)

    @staticmethod
    def get_first_signal_markup() -> InlineKeyboardMarkup:
        first_signal = InlineKeyboardButton('СИГНАЛ MINES 💣', callback_data='next_signal')
        return InlineKeyboardMarkup(row_width=2).add(first_signal)

    @staticmethod
    def get_next_signal_markup() -> InlineKeyboardMarkup:
        next_signal = InlineKeyboardButton('💣 СЛЕДУЮЩИЙ СИГНАЛ ➡', callback_data='next_signal')
        return InlineKeyboardMarkup(row_width=2).add(next_signal)

