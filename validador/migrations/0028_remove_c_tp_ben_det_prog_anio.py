# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0027_auto_20170327_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_tp_ben_det_prog',
            name='ANIO',
        ),
    ]
