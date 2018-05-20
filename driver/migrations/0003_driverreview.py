# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_auto_20180520_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField()),
                ('driver_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.DriverProfile')),
            ],
        ),
    ]