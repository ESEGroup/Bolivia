# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('registro_ufrj', models.CharField(max_length=8)),
                ('idade', models.PositiveIntegerField()),
                ('departamento', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('chefe_departamento', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='vaga',
            name='disponibilidade',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vaga',
            name='remuneracao',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='vaga',
            name='tipo',
            field=models.CharField(max_length=4, default='EE', choices=[('IC', 'Iniciacao Cientifica'), ('EE', 'Estagio externo'), ('EI', 'Estagio interno'), ('PROJ', 'Projeto')]),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='prazo_de_aplicacao',
            field=models.DateField(),
        ),
    ]
