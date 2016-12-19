# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0034_auto_20161214_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='candidatos',
            field=models.ManyToManyField(blank=True, to='sistema.Profile', related_name='_candidatos_+'),
        ),
    ]
