from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from locations.models import Geolocation
from locations.serializers import GeolocationSerializer
from locations.services.ipstack import IPStackConnector


class GeolocationViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all()

    def create(self, request, *args, **kwargs):
        ip = self.request.data.get("ip")
        ip_stack_connector = IPStackConnector(ip)
        data = ip_stack_connector.get_data()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)