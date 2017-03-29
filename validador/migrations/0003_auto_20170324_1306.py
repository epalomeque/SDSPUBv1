# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0002_auto_20170324_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_a_subprog',
            name='CVE_SUBPROGRAMA',
            field=models.CharField(max_length=5),
        ),
    ]
