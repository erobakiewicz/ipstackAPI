from django.test import TestCase

from locations.services.ipstack import IPStackConnector, IPStackConnectorError


class LocationsTestCase(TestCase):

    def test_get_clean_ip_raises_error_for_no_ip(self):
        wrong_ip = "192.0.1asd"
        with self.assertRaises(IPStackConnectorError):
            IPStackConnector.get_clean_ip(wrong_ip)

    def test_get_clean_ip_returns_proper_ip(self):
        str_contains_proper_ip = "https://162.12.206.5/"
        proper_ip = IPStackConnector.get_clean_ip(str_contains_proper_ip)
        self.assertEqual(proper_ip, '162.12.206.5')
