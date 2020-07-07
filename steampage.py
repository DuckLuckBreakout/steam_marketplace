import requests


class SteamPage:
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 ' \
                 'YaBrowser/20.4.3.268 (beta) Yowser/2.5 Safari/537.36'

    def __init__(self, url):
        headers = {'User-Agent': self.user_agent}
        self.page = requests.get(url, headers=headers)
        self.html = self.page.text
