# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0027_auto_20161211_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='candidato_selecionado',
            field=models.OneToOneField(to='sistema.Profile', null=True, related_name='+'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='candidatos',
            field=models.ManyToManyField(to='sistema.Profile', null=True, related_name='_candidatos_+'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='professor_responsavel',
            field=models.ForeignKey(to='sistema.Profile', null=True),
        ),
    ]
