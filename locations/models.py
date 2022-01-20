from django.db import models


class Geolocation(models.Model):
    ip = models.CharField("ip address", max_length=39, unique=True)
    continent_code = models.CharField("continent code", max_length=5)
    continent_name = models.CharField("continent name", max_length=50)
    country_name = models.CharField("country name", max_length=100)
    city = models.CharField("city", max_length=250, blank=True)

    class Meta:
        verbose_name = 'Geolocation'
        verbose_name_plural = 'Geolocations'

    def __str__(self):
        return f'{self.ip}: {self.country_name}'
