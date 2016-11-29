# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_auto_20161124_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 1, 39, 24, 606712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='prazo_de_aplicacao',
            field=models.DateField(default=datetime.date(2016, 11, 28)),
        ),
    ]
