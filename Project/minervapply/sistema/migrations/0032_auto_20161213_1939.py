# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0031_remove_vaga_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='tipo',
            field=models.CharField(choices=[('Iniciacao Cientifica', 'Iniciacao Cientifica'), ('Estagio externo', 'Estagio externo'), ('Estagio interno', 'Estagio interno'), ('Projeto', 'Projeto')], max_length=4, default='Estagio externo'),
        ),
    ]
