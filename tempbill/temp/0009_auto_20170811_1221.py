# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tempbill', '0008_billitem_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billitem',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='billitem',
            name='medicine',
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='BillItem',
        ),
    ]
