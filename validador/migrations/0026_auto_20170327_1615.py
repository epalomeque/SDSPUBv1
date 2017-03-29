# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0025_auto_20170327_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_beneficio',
            name='NB_BENEFICIO',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='c_beneficio',
            name='SEUSAEN',
            field=models.CharField(max_length=150),
        ),
    ]
