# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0034_remove_c_tp_beneficio_prog_cd_tp_beneficio'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_tp_beneficio_prog',
            name='CD_TP_BENEFICIO',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
