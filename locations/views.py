from django.http import JsonResponse
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from locations.models import Geolocation
from locations.serializers import GeolocationSerializer
from locations.services.ipstack import IPStackConnector, IPStackConnectorError


class GeolocationViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        ip = self.request.data.get("ip")
        try:
            ip_stack_connector = IPStackConnector(ip)
        except IPStackConnectorError as e:
            return JsonResponse(status=401, data=e.get_full_details())
        data = ip_stack_connector.get_data()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
