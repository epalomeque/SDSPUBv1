# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0006_auto_20170324_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_beneficio_ob_prog',
            name='NB_BENEFICIO_OB',
            field=models.CharField(max_length=120),
        ),
    ]
