# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0033_auto_20161213_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='candidato_selecionado',
            field=models.ForeignKey(blank=True, to='sistema.Profile', related_name='+', null=True),
        ),
    ]
