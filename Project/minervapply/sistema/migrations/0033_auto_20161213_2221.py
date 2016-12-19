# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0032_auto_20161213_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='tipo',
            field=models.CharField(default='EE', max_length=4, choices=[('IC', 'Iniciacao Cientifica'), ('EE', 'Estagio externo'), ('EI', 'Estagio interno'), ('PROJ', 'Projeto')]),
        ),
    ]
