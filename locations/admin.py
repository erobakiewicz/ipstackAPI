from django.contrib import admin

from locations.models import Geolocation


@admin.register(Geolocation)
class GeolocationAdmin(admin.ModelAdmin):
    pass
