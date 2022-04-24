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

        if r.status_code != 200:
            raise APIError(response['message'])

        return response

    def get_listed_info(self, code:str = None):
        params = {'code': code}
        url = '/listed/info'
        return self._call(url, 'get', **params)

    def get_listed_sections(self):
        url = '/listed/sections'
        return self._call(url, 'get')

    def get_daily_quotes(
            self, code:str = None, from_d:str = None,
            to_d:str = None, date:str = None
        ):
        params = {'code': code, 'from': from_d, 'to': to_d, 'date': date}
        url = '/prices/daily_quotes'
        return self._call(url, 'get', **params)

    def get_fins_statements(self, code:str = None, date:str = None):
        params = {'code': code, 'date': date}
        url = '/fins/statements'
        return self._call(url, 'get', **params)

    def get_fins_announcement(self):
        url = '/fins/announcement'
        return self._call(url, 'get')