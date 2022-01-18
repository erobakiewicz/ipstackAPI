from django.db import models


class Geolocation(models.Model):
    ip = models.CharField(max_length=39, verbose_name="ip address")
    continent_code = models.CharField(max_length=5, verbose_name="continent code")
    continent_name = models.CharField(max_length=50, verbose_name="continent name")
    country_name = models.CharField(max_length=100, verbose_name='country name')
    city = models.CharField(max_length=250, verbose_name='city')

    def __str__(self):
        return f'{self.ip}: {self.country_name}'
