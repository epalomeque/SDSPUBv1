# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0032_auto_20170328_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_tp_beneficio_prog',
            name='CD_TP_BENEFICIO',
            field=models.CharField(max_length=12),
        ),
    ]
