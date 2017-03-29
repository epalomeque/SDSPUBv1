# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0007_auto_20170324_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_periodo',
            name='FRASE',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='c_periodo',
            name='NOTA',
            field=models.CharField(max_length=255),
        ),
    ]
