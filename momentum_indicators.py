import talib


def ROC(data, timeperiod=10):
    return talib.ROC(data['close'], timeperiod=timeperiod)


def RSI(data, timeperiod=14):
    return talib.RSI(data['close'], timeperiod=timeperiod)


def STOCH(data, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    return talib.STOCH(data['high'], data['low'], data['close'], fastk_period=fastk_period, slowk_period=slowk_period,
                       slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)


def MACD(data, fastperiod=12, slowperiod=26, signalperiod=9):
    return talib.MACD(data['close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)


def STOCHRSI(data, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    return talib.STOCHRSI(data['close'], timeperiod=timeperiod, fastk_period=fastk_period,
                          fastd_period=fastd_period, fastd_matype=fastd_matype)

def BBANDS(data, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0):
    return talib.BBANDS(data['close'], timeperiod=timeperiod, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
