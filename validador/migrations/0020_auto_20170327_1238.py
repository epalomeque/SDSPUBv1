# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0019_auto_20170327_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_programa',
            name='NB_PROG',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='c_programa',
            name='NB_PROGRAMA',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='c_programa',
            name='NB_SUBP1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='c_programa',
            name='NB_SUBP2',
            field=models.CharField(max_length=150),
        ),
    ]
