# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0015_auto_20161129_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 4, 24, 47, 82275, tzinfo=utc)),
        ),
    ]
