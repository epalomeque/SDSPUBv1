# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validador', '0017_auto_20170324_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_intraprogramas',
            name='CVE_INTRAPROGRAMA',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='c_intraprogramas',
            name='NB_DEPENDENCIA',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='c_intraprogramas',
            name='NB_PROGRAMA',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='c_intraprogramas',
            name='NB_UR',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='c_intraprogramas',
            name='TP_INTRAPROGRAMA',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
