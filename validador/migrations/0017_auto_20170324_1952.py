# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0016_auto_20170324_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_beneficio_prog',
            name='SEUSAEN',
        ),
        migrations.AlterField(
            model_name='c_beneficio_prog',
            name='NB_BENEFICIO',
            field=models.CharField(max_length=200),
        ),
    ]
