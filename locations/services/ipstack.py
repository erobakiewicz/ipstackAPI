import re
import requests

from django.conf import settings
from rest_framework.exceptions import APIException

IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
BASE_URL = f'http://api.ipstack.com/'


class IPStackConnectorError(APIException):
    default_detail = 'Service temporarily unavailable, try again later.'


class IPStackConnector:

    def __init__(self, ip):
        self.ip = self.get_clean_ip(ip)
        self.ipstack_url = f'{BASE_URL}{self.ip}?access_key={settings.IPSTACK_ACCESS_KEY}'

    def get_data(self):
        """
        Takes ip stack endpoint url with IP address and returns in response IP geolocation data.
        """
        response = requests.get(
            url=self.ipstack_url,
        )
        if response.status_code != 200:
            raise IPStackConnectorError(f'Failed, status code {response.status_code}, reason: {response.json()}')
        return response.json()

    @staticmethod
    def get_clean_ip(ip):
        """
        Takes str and checks if it contains valid IP address and returns just the IP omitting rest of str.
        If no valid IP address error is raised.
        """
        if valid_ip := (re.findall(IP_REGEX, ip)):
            return valid_ip[0]
        else:
            raise IPStackConnectorError("This is not valid IP address!")
