# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0020_auto_20161129_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='telefone',
            field=models.CharField(max_length=20, default='0000-0000'),
        ),
    ]
