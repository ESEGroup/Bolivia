# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20161114_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='titulo',
            field=models.CharField(max_length=200, default='Titulo Vaga'),
        ),
    ]
