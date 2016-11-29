# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0012_auto_20161128_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 2, 15, 36, 710502, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='prazo_de_aplicacao',
            field=models.DateField(default=datetime.date(2016, 11, 29)),
        ),
    ]
