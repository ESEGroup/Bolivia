# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0029_auto_20161212_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
