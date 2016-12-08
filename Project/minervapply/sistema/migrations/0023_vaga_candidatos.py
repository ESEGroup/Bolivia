# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0022_auto_20161130_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='candidatos',
            field=models.ManyToManyField(related_name='_candidatos_+', to='sistema.Profile'),
        ),
    ]
