import os
import random

from aiogram.types import InputFile
from aiogram.utils.markdown import quote_html

from config import Config


class Messages:
    # Статья с фото:  https://telegra.ph/Resources-Mines-John-01-12

    @staticmethod
    def get_loading() -> str:
        return '♻ Загрузка...'

    @staticmethod
    def ask_for_locale() -> str:
        return 'Выберите язык ⬇ \n' \
               'Choose your language ⬇'

    @staticmethod
    def get_welcome(user_name: str = 'незнакомец') -> str:
        return (
            '<b>БОТ НА ИГРУ MINES 1WIN💣</b> \n\n'
            '💸 Заработок от <b>50-100$</b> ежедневно! 💸 \n\n'
            '<b>Бот активируется</b> только на тех аккаунтах, которые были пополнены на любую сумму. '
            '<b>Искусственный интеллект</b>, прозрачная система. '
            'Пополнив баланс, поступит <b>Пароль</b>, который вам нужно написать сюда и начать зарабатывать!\n\n'
            '<b>👇 Жмите кнопку, если все понятно!</b>'
        ).format(user_name=quote_html(user_name))

    @staticmethod
    def get_welcome_photo_url() -> str:
        return 'https://telegra.ph/file/19b3334d24d48a5c890f2.png'

    @staticmethod
    def get_after_welcome_explanation() -> str:
        return (
            '<b><i>️#️⃣ Важно</i></b>\n\n'
            'Чтобы бот работал на <b><i>100%</i></b> \n'
            'Выставляем в игре <b><i>3 ловушки</i></b>, не больше и не меньше. \n'
            '<b><i>Играем на трех 💣</i></b>'
        )

    @staticmethod
    def get_after_welcome_explanation_photo() -> str:
        return 'https://telegra.ph/file/595eb08ffd1986ce39a4f.png'

    @staticmethod
    def get_before_game_start() -> str:
        return (
            'ЕСЛИ БОТ ВЫДАЕТ НЕ ВЕРНЫЕ СИГНАЛЫ, ЗНАЧИТ БОТ НЕ АКТИВИРОВАЛСЯ. \n'
            'ПОПОЛНИТЕ БАЛАНС ЕЩЕ РАЗ НА 1000₽ И БОТ ЗАРАБОТАЕТ НА 100%💸🤖 \n\n'
            'ЖМИ ⬇⬇⬇'
        )

    @staticmethod
    def get_before_game_start_photo() -> str:
        return 'https://telegra.ph/file/b7abff1b3ce156a61266c.png'

    @staticmethod
    def ask_for_code_word() -> str:
        return '<b>✅ ВВЕДИТЕ ПАРОЛЬ:</b>'

    @staticmethod
    def get_code_word_incorrect():
        return '❗Неверный пароль, попробуйте ещё раз:'

    # @staticmethod
    # def ask_for_1win_id() -> str:
    #     return (
    #         '<b>Напишите свой айди аккаунта \n'
    #         'который активировался после \n'
    #         'пополнения баланса 🆔</b> \n'
    #         '<i>(пример: 58367211)</i>'
    #     )
    #
    # @staticmethod
    # def get_1win_id_incorrect_length() -> str:
    #     return '❗ID должен иметь длину в 8 или 9 цифр. Попробуйте снова:'
    #
    # @staticmethod
    # def get_1win_id_have_forbidden_symbols() -> str:
    #     return '❗ID может состоять только из цифр. Попробуйте снова:'

    @staticmethod
    def get_throttled_error() -> str:
        return 'Пожалуйста, не так часто 🙏'

    @staticmethod
    def get_random_signal() -> InputFile:
        images_dir_path = Config.SIGNALS_IMAGES_DIR
        files = [
            filename for filename in os.listdir(images_dir_path)
            if filename.endswith('.png')
        ]

        random_filename = random.choice(files)
        return InputFile(path_or_bytesio=os.path.join(images_dir_path, random_filename))
