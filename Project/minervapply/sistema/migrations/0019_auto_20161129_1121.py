# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0018_auto_20161129_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='data_publicacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
