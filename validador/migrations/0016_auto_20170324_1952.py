# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0015_auto_20170324_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_beneficio_as_prog',
            name='NB_BENEFICIO_AS',
            field=models.CharField(max_length=150),
        ),
    ]
