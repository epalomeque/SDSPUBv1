# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0028_remove_c_tp_ben_det_prog_anio'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_tp_ben_det_prog',
            name='ANIO',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
