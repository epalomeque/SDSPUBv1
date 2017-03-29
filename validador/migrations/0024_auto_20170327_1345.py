# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0023_c_programa_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_tp_ben_det',
            name='NB_TP_BEN_DET',
            field=models.CharField(max_length=120),
        ),
    ]
