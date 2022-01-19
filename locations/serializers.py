from rest_framework import serializers

from locations.models import Geolocation


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['id', 'ip', 'continent_code', 'continent_name', 'country_name', 'city']
