import pandas
import numpy
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_finance import candlestick2_ohlc
from skin import Skin
import momentum_indicators
import steampage


class SkinAnalyst:
    steam_market_url = 'https://steamcommunity.com/market/'

    def __init__(self, skin: Skin):
        self.skin = skin
        self.url = self.get_url()
        self.market_data = self.get_market_data()

    def get_url(self):
        url = f'{self.steam_market_url}/listings/{self.skin.app_id}/{self.skin.name}'
        return url

    def get_market_data(self):
        with open('page.html', 'w') as html:
            html.write(steampage.SteamPage(self.url).html)

        with open('page.html', 'r') as html:
            for line in html:
                if 'var line1' in line:
                    data = eval(line[13:-2])

        for i in range(len(data)):
            tmp = data[i][0].split()
            if tmp[3] != '01:':
                return data[i:]

    def get_dataframe(self, indicators: list):
        data = {'open': numpy.asarray([item[1] for item in self.market_data[:-1]]),
                'close': numpy.asarray([item[1] for item in self.market_data[1:]]),
                'date': numpy.asarray([item[0] for item in self.market_data[1:]])}

        data['high'] = numpy.asarray(
            [max(open_price, close_price) for open_price, close_price in zip(data['open'], data['close'])])
        data['low'] = numpy.asarray(
            [min(open_price, close_price) for open_price, close_price in zip(data['open'], data['close'])])

        for indicator in indicators:
            tmp_data = indicator(data)
            if isinstance(tmp_data, tuple):
                i = 0
                for arr in tmp_data:
                    data[f'{indicator.__name__}{i}'] = arr
            else:
                data[indicator.__name__] = tmp_data
        return data

    def get_graphs(self, indicators: list):
        data = self.get_dataframe(indicators)
        xdate = [datetime.fromtimestamp(datetime.strptime(str(date[:-3]), '%b %d %Y %H:').timestamp()) \
                 for date in data['date']]

        fig, ax = plt.subplots(len(data.keys()) - 4 + 1, sharex=True, dpi=1000)

        candlestick2_ohlc(ax[0], data['open'], data['high'], data['low'], data['close'], width=0.6)

        ax[0].xaxis.set_major_locator(ticker.MaxNLocator(20))

        def chart_date(x, pos):
            try:
                return xdate[int(x)]
            except IndexError:
                return ''

        ax[0].xaxis.set_major_formatter(ticker.FuncFormatter(chart_date))

        fig.autofmt_xdate()
        fig.tight_layout()

        i = 1
        for indicator in list(data.keys())[4:]:
            ax[i].plot(data[indicator])
            i += 1

        plt.show()
        fig.savefig(self.skin.name)