# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0021_auto_20170327_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_programa',
            name='ANIO',
        ),
    ]
