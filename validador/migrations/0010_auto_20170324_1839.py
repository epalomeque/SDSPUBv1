# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0009_auto_20170324_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_ur',
            name='NB_UR',
            field=models.CharField(max_length=120),
        ),
    ]
