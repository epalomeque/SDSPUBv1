# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0035_c_tp_beneficio_prog_cd_tp_beneficio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_tp_beneficio_prog',
            name='CD_PROG_DGGPB',
            field=models.CharField(max_length=70),
        ),
    ]
