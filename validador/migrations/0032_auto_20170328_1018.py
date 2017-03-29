# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0031_auto_20170328_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_id_grupo',
            name='NB_GRUPO_ID',
            field=models.CharField(max_length=120),
        ),
    ]
