# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0026_auto_20170327_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_programa_dgtic',
            name='NB_PROGRAMA',
            field=models.CharField(max_length=150),
        ),
    ]
