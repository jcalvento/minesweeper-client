import os

from requests import post, put, get


class MinesweeperApi:
    DEFAULT_URL = 'https://frozen-citadel-76869.herokuapp.com'

    def __init__(self, base_url):
        os.environ['no_proxy'] = '127.0.0.1,localhost'
        self._base_url = base_url or self.DEFAULT_URL

    def create(self, params):
        return post(url=self._api_url('games'), headers=self._headers(), data=params)

    def update(self, game_id, params):
        return put(url=self._api_url(f'games/{game_id}'), headers=self._headers(), data=params)

    def index(self):
        return get(url=self._api_url('games'), headers=self._headers())

    def show(self, game_id):
        return get(url=self._api_url(f'games/{game_id}'), headers=self._headers())

    def _headers(self):
        return {'Accept': 'application/json'}

    def _api_url(self, path):
        return f"{self._base_url}/{path}"
