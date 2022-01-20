from django.http import JsonResponse
from rest_framework import viewsets

from locations.models import Geolocation
from locations.serializers import GeolocationSerializer, IPSerializer
from locations.services.ipstack import IPStackConnector, IPStackConnectorError, IP_REGEX


class GeolocationViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'create': IPSerializer,
    }
    default_serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all()
    lookup_field = 'ip'
    lookup_value_regex = IP_REGEX

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer):
        ip = serializer.data.get('ip')
        try:
            ip_stack_connector = IPStackConnector(ip)
        except IPStackConnectorError as e:
            return JsonResponse(status=401, data=e.get_full_details())
        data = ip_stack_connector.get_data()
        serializer = self.default_serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
