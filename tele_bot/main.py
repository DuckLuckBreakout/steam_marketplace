import telebot
from constants import TELETOKEN, MY_ID
import tele_bot.keyboards as keyboards

from skin import Skin
from skin_analyst import SkinAnalyst

import telebot
from telebot.types import Message
from constants import TELETOKEN, MY_ID
from momentum_indicators import *
from skin import Skin
from skin_analyst import SkinAnalyst


indicators = []
skin_name = ''

status = ''
bot = telebot.TeleBot(TELETOKEN)


def send_text_message(to_user_id, message, keyboard=keyboards.MenuKeyboard):
    bot.send_message(to_user_id, message, reply_markup=keyboard())


def send_file_message(to_user_id, filename):
    with open(filename, 'rb') as file:
        bot.send_document(to_user_id, file)


def send_main_menu_message(to_user_id):
    message = 'Главное меню:'
    send_text_message(to_user_id, message, keyboards.MainMenuKeyboard)


def send_skin_analysis_message(to_user_id):
    message = 'Введи название скина:'
    send_text_message(to_user_id, message, keyboards.SkinAnalysisMenuKeyboard)


def send_input_indicators_message(to_user_id):
    message = 'Введи индикатор:'
    send_text_message(to_user_id, message, keyboards.InputIndicatorsMenuKeyboard)


def send_input_skin_message(to_user_id):
    message = 'Введи название скина:'
    send_text_message(to_user_id, message, keyboards.InputIndicatorsMenuKeyboard)


def send_result_message(to_user_id, filename):
    message = 'Результат:'
    send_text_message(to_user_id, message, keyboards.MainMenuKeyboard)
    send_file_message(to_user_id, filename)


def get_result(to_user_id):
    test_skin = Skin(name=skin_name, app_id=730)
    analyst = SkinAnalyst(test_skin)
    indicators_result = analyst.get_graphs(indicators)
    send_result_message(to_user_id, f'{skin_name}.png')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global status

    if status == '':
        if message.text == '/start':
            send_main_menu_message(message.from_user.id)
            status = 'main_menu'
        else:
            send_text_message(message.from_user.id, 'Напиши /start для начала работы')

    elif status == 'main_menu':
        if message.text == 'Анализ скина':
            send_skin_analysis_message(message.from_user.id)
            status = 'skin_input'

        elif message.text == 'В главное меню':
            status = 'main_menu'
            send_main_menu_message(message.from_user.id)

        else:
            send_text_message(message.from_user.id, 'Неверная команда')

    elif status == 'skin_input':
        if message.text == 'В главное меню':
            status = 'main_menu'
            send_main_menu_message(message.from_user.id)

        else:
            global skin_name
            skin_name = message.text
            status = 'skin_analysis'
            send_input_indicators_message(message.from_user.id)

    elif status == 'skin_analysis':
        if message.text == 'Получить результат':
            get_result(message.from_user.id)
            status = 'main_menu'
            send_main_menu_message(message.from_user.id)

        elif message.text == 'В главное меню':
            status = 'main_menu'
            send_main_menu_message(message.from_user.id)

        else:
            global indicators
            indicators.append(eval(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
