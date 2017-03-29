# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0033_auto_20170328_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_tp_beneficio_prog',
            name='CD_TP_BENEFICIO',
        ),
    ]
