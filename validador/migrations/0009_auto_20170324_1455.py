# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0008_auto_20170324_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_periodo',
            name='FRASE',
        ),
        migrations.RemoveField(
            model_name='c_periodo',
            name='NOTA',
        ),
    ]
