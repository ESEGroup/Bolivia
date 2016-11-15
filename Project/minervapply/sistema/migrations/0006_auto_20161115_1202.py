# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_vaga_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='prazo_de_aplicacao',
            field=models.DateField(default=datetime.date(2016, 11, 15)),
        ),
    ]
