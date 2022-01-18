from rest_framework import viewsets, mixins
from locations.models import Geolocation
from locations.serializers import GeolocationSerializer


class GeolocationViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all()
