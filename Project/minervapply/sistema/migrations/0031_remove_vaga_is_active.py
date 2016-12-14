# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0030_vaga_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='is_active',
        ),
    ]
