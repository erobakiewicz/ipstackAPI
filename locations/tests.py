from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, force_authenticate
from locations.services.ipstack import IPStackConnector, IPStackConnectorError


class LocationsTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.user = User.objects.create_user(username="test_user", password="test_password")

    def setUp(self):
        self.token = self.get_access_token()

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

    def test_geolcation_viewset_authentication_provided(self):
        self.client.credentials(**{'Authorization': 'Bearer {}'.format(self.token)})
        self.client.force_authenticate(user=self.user, token=self.token)

        response = self.client.get("/geolocations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def get_access_token(self):
        response = self.client.post(
            "/token/",
            data={'username': "test_user", "password": "test_password"},
            format="json"
        )
        return response.data.get('access')
