import re
import requests

from django.conf import settings

IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
BASE_URL = f'http://api.ipstack.com/'


class IPStackConnectorError(Exception):
    pass


class IPStackConnector:

    def __init__(self, ip):
        self.ip = self.get_clean_ip(ip)
        self.ipstack_url = f'{BASE_URL}{self.ip}?access_key={settings.IPSTACK_ACCESS_KEY}'

    def get_data(self):
        response = requests.get(
            url=self.ipstack_url,
        )
        if response.status_code != 200:
            raise IPStackConnectorError
        return response.json()

    @staticmethod
    def get_clean_ip(ip):
        if valid_ip := (re.findall(IP_REGEX, ip)):
            return valid_ip[0]
        else:
            raise IPStackConnectorError("This is not valid IP address!")
