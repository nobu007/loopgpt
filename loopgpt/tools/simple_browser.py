"""
Adapted from Auto-GPT (https://github.com/Significant-Gravitas/Auto-GPT)
"""


import atexit

import requests
from bs4 import BeautifulSoup
from loopgpt.summarizer import Summarizer
from loopgpt.tools.browser import Browser


class SimpleBrowser(Browser):
    """デフォルトの Google Chrome 実装の代わりにリクエスト ライブラリを使用する代替ブラウザ実装です。

    Usage:

    ```
    import loopgpt
    agent = loopgpt.Agent(...)
    agent.tools["browser"] = SimpleBrowser()
    ```
    """

    def __init__(self):
        super(SimpleBrowser, self).__init__()
        session = requests.Session()
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
            }
        )
        self.session = session
        self.summarizer = Summarizer()
        self.cache = {}

    def _get(self, url):
        if url in self.cache:
            return self.cache[url]
        resp = self.session.get(url)
        if resp.status_code >= 400:
            return f"HTTP Error {resp.status_code}"
        self.cache[url] = resp.text
        return resp.text

    @property
    def id(self):
        return "browser"
