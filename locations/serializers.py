from rest_framework import serializers

from locations.models import Geolocation


class IPSerializer(serializers.Serializer):
    ip = serializers.IPAddressField()


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['ip', 'continent_code', 'continent_name', 'country_name', 'city']
