# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0005_auto_20170324_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_beneficio_ob',
            name='NB_BENEFICIO_OB',
            field=models.CharField(max_length=120),
        ),
    ]
