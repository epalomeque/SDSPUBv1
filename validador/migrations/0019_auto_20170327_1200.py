# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0018_auto_20170327_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_intraprogramas',
            name='NB_INTRAPROGRAMA',
            field=models.CharField(max_length=150),
        ),
    ]
