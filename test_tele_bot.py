import telebot
from telebot.types import Message
from constants import TELETOKEN, MY_ID
from momentum_indicators import *
from skin import Skin
from skin_analyst import SkinAnalyst


indicators = []
skin_name = ''

status = 'main_menu'


bot = telebot.TeleBot(TELETOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Построить графики')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('ROC', 'RSI', 'STOCH')
keyboard2.row('MACD', 'STOCHRSI', 'BBANDS')
keyboard2.row('Построить графики')
keyboard2.row('В главное меню')

keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('В главное меню')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global status
    global skin_name
    if status == 'main_menu':
        if message.text == "Построить графики":
            bot.send_message(message.from_user.id, "Введи название скина:")
            status = 'check_skin'
        else:
            bot.send_message(message.from_user.id, 'Ошибка в команде', reply_markup=keyboard1)

    elif status == 'check_skin':
        skin_name = message.text
        bot.send_message(message.from_user.id, "Введи название индикатора:", reply_markup=keyboard2)
        status = 'indicators_input'

    elif status == 'indicators_input':
        if message.text == "Построить графики":
            test_skin = Skin(name=skin_name, app_id=730)
            analyst = SkinAnalyst(test_skin)
            indicators_result = analyst.get_graphs_BBANDS(indicators)
            with open(f'{skin_name}.png', 'rb') as result:
                bot.send_message(message.from_user.id, "Результат получен:")
                bot.send_document(message.from_user.id, result)
                bot.send_message(message.from_user.id, str(indicators_result), reply_markup=keyboard3)

            status = 'main_menu'
        else:
            indicators.append(eval(message.text))
            print(indicators)


bot.polling(none_stop=True, interval=0)
