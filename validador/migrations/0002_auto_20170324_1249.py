# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_a_subprog',
            name='NB_AP_SUBPROG',
            field=models.CharField(max_length=120),
        ),
    ]
