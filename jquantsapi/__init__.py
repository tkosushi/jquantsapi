import requests


class APIError(Exception):
    pass

class API(object):
    def __init__(self, token: str):
        self._base_url = 'https://api.jpx-jquants.com/v1'
        if token:
            self.headers = {'Authorization': 'Bearer {}'.format(token)}
        else:
            raise APIError('No API token specified.')

    def _call(self, url: str, method: str, **params: dict):
        r = None
        url = self._base_url + url
        if method == 'get':
            r = requests.get(url, params=params, headers=self.headers)
        elif method == 'post':
            r = requests.post(url, data=params, headers=self.headers)
        response = r.json()

        return response

    def get_listed_info(self):
        url = '/listed/info'
        return self._call(url, 'get')

    def get_listed_sections(self):
        url = '/listed/sections'
        return self._call(url, 'get')

    def get_daily_quotes(self, code: str):
        params = {'code': code}
        url = '/prices/daily_quotes'
        return self._call(url, 'get', **params)

    def get_fins_statements(self, code: str):
        params = {'code': code}
        url = '/fins/statements'
        return self._call(url, 'get', **params)

    def get_fins_announcement(self):
        url = '/fins/announcement'
        return self._call(url, 'get')