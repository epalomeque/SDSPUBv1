# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0012_auto_20170324_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_actividades',
            name='NB_ACTIV_ECONO',
            field=models.CharField(max_length=255),
        ),
    ]
