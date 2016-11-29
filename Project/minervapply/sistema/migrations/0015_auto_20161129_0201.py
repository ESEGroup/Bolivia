# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema', '0014_auto_20161129_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='chefe_departamento',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='idade',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='registro_ufrj',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='url',
        ),
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vaga',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 3, 59, 38, 872698, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='professor_responsavel',
            field=models.ForeignKey(blank=True, null=True, to='sistema.Professor'),
        ),
    ]
