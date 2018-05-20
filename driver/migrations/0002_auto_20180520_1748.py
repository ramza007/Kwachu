# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='car-image/'),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='driver/profile-pic'),
        ),
    ]
