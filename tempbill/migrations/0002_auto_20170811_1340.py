# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempbill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]