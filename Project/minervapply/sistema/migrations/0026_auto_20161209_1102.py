# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0025_auto_20161209_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dre',
            field=models.CharField(max_length=9, default='000000000'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='registro_ufrj',
            field=models.CharField(max_length=9, default='000000000'),
        ),
    ]
