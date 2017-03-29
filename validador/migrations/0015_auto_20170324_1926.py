# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0014_auto_20170324_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_ap_desc',
            name='NB_ISUBPROGRAMA',
            field=models.CharField(max_length=255),
        ),
    ]
