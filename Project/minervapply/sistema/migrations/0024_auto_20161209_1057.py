# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0023_vaga_candidatos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registro_ufrj',
            field=models.CharField(default='000000000', max_length=8),
        ),
    ]
