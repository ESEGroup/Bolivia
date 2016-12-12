# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0028_auto_20161211_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='candidato_selecionado',
            field=models.OneToOneField(to='sistema.Profile', related_name='+', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='candidatos',
            field=models.ManyToManyField(to='sistema.Profile', related_name='_candidatos_+', null=True, blank=True),
        ),
    ]
