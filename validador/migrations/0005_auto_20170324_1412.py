# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0004_auto_20170324_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_beneficio_as',
            name='NB_BENEFICIO_AS',
            field=models.CharField(max_length=255),
        ),
    ]
