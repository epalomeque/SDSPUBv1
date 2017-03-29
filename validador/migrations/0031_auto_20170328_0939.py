# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0030_auto_20170327_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estructurapersonas',
            name='IN_CORRESP',
            field=models.ForeignKey(verbose_name=b'Indicador del cumplimiento de la corresponsabilidad', to='validador.C_CORRESP'),
        ),
    ]
