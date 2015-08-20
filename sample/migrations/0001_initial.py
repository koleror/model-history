# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('boolean', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
