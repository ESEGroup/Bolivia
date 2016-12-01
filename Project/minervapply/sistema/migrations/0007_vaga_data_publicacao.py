# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_auto_20161115_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.date(2016, 11, 15)),
        ),
    ]
