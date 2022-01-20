from unittest.mock import patch

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient, APITestCase

from locations.models import Geolocation
from locations.services.ipstack import IPStackConnector, IPStackConnectorError


class LocationsTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.user = User.objects.create_user(username="test_user", password="test_password")

    def test_get_clean_ip_raises_error_for_no_ip(self):
        wrong_ip = "192.0.1asd"
        with self.assertRaises(IPStackConnectorError):
            IPStackConnector.get_clean_ip(wrong_ip)

    def test_get_clean_ip_returns_proper_ip(self):
        str_contains_proper_ip = "https://162.12.206.5/"
        proper_ip = IPStackConnector.get_clean_ip(str_contains_proper_ip)
        self.assertEqual(proper_ip, '162.12.206.5')

    def test_geolocation_viewset_authentication_not_provided(self):
        response = self.client.get("/geolocations/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_authentication_token(self):
        response = self.client.post(
            "/token/",
            data={'username': "test_user", "password": "test_password"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_geolcation_viewset_raises_wrong_ip(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/geolocations/", data={"ip": "wrong_ip"}, format='json')
        self.assertEqual(response.data.get("ip")[0],
                         ErrorDetail(string='Enter a valid IPv4 or IPv6 address.', code='invalid'))

    @patch('locations.services.ipstack.IPStackConnector.get_data')
    def test_geolcation_viewset_creates_geolocation_object_based_on_ip(self, mock_ip_stack):
        mock_ip_stack.return_value = {
            "ip": "84.10.2.58",
            "type": "ipv4",
            "continent_code": "EU",
            "continent_name": "Europe",
            "country_code": "PL",
            "country_name": "Poland",
            "region_code": "PM",
            "region_name": "Pomerania",
            "city": "Sopot",

        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/geolocations/", data={"ip": "84.10.2.58"}, format='json')
        self.assertTrue(Geolocation.objects.get(ip="84.10.2.58"))
