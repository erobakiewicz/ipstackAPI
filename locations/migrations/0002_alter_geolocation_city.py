# Generated by Django 4.0.1 on 2022-01-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='city',
            field=models.CharField(blank=True, max_length=250, verbose_name='city'),
        ),
    ]
