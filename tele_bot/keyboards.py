import telebot


class MenuKeyboard(telebot.types.ReplyKeyboardMarkup):
    rows = [['/start']]

    def __init__(self):
        super().__init__(resize_keyboard=True)
        [self.row(*row) for row in self.rows]


class MainMenuKeyboard(telebot.types.ReplyKeyboardMarkup):
    rows = [['Анализ скина']
            ]

    def __init__(self):
        super().__init__(resize_keyboard=True)
        [self.row(*row) for row in self.rows]


class SkinAnalysisMenuKeyboard(telebot.types.ReplyKeyboardMarkup):
    rows = [['Gamma 2 Case'],
            ['В главное меню']
            ]

    def __init__(self):
        super().__init__(resize_keyboard=True)
        [self.row(*row) for row in self.rows]


class InputIndicatorsMenuKeyboard(telebot.types.ReplyKeyboardMarkup):
    rows = [['ROC', 'RSI', 'STOCH'],
            ['MACD', 'STOCHRSI', 'BBANDS'],
            ['Получить результат'],
            ['В главное меню']
            ]

    def __init__(self):
        super().__init__(resize_keyboard=True)
        [self.row(*row) for row in self.rows]
