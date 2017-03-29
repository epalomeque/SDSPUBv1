# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0024_auto_20170327_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_tp_ben_det',
            name='SEUSAEN',
            field=models.CharField(max_length=200),
        ),
    ]
