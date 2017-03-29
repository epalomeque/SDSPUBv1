# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0020_auto_20170327_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_programa',
            name='CD_PROGRAMA',
            field=models.CharField(max_length=10),
        ),
    ]
