# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_vaga_professor_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='departamento',
            field=models.CharField(max_length=200, default='nome_departamento'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.EmailField(max_length=254, default='email@email.com'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='idade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=100, default='nome'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='registro_ufrj',
            field=models.CharField(max_length=8, default='000000-0'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='telefone',
            field=models.CharField(max_length=20, default='0000-0000'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='url',
            field=models.URLField(default='www.default.com'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='local',
            field=models.CharField(max_length=200, default='local'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='prazo_de_aplicacao',
            field=models.DateField(default=datetime.date(2016, 11, 14)),
        ),
    ]
