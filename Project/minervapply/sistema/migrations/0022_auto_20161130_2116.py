# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema', '0021_professor_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data_nascimento', models.DateField(null=True, blank=True)),
                ('telefone', models.CharField(max_length=20, default='0000-0000')),
                ('is_aluno', models.BooleanField(default=False)),
                ('is_professor', models.BooleanField(default=False)),
                ('registro_ufrj', models.CharField(max_length=8, default='000000-0')),
                ('departamento', models.CharField(max_length=200, default='nome_departamento')),
                ('url', models.URLField(default='www.default.com')),
                ('chefe_departamento', models.BooleanField(default=False)),
                ('curso', models.CharField(max_length=200, default='curso')),
                ('dre', models.CharField(max_length=8, default='000000-0')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='professor',
            name='user',
        ),
        migrations.AlterField(
            model_name='vaga',
            name='professor_responsavel',
            field=models.ForeignKey(null=True, blank=True, to='sistema.Profile'),
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
    ]
