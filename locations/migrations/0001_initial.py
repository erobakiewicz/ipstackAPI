# Generated by Django 4.0.1 on 2022-01-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=39, verbose_name='ip address')),
                ('continent_code', models.CharField(max_length=5, verbose_name='continent code')),
                ('continent_name', models.CharField(max_length=50, verbose_name='continent name')),
                ('country_name', models.CharField(max_length=100, verbose_name='country name')),
                ('city', models.CharField(max_length=250, verbose_name='city')),
            ],
        ),
    ]
