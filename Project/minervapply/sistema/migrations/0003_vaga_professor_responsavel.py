# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20161114_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='professor_responsavel',
            field=models.ForeignKey(default=0, to='sistema.Professor'),
        ),
    ]
