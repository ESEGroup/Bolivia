# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0026_auto_20161209_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='candidato_selecionado',
            field=models.OneToOneField(blank=True, to='sistema.Profile', related_name='+', null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='candidatos',
            field=models.ManyToManyField(blank=True, to='sistema.Profile', related_name='_candidatos_+', null=True),
        ),
    ]
