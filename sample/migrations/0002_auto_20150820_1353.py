# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleFK',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='link',
            field=models.ForeignKey(default=None, blank=True, to='sample.SampleFK', null=True),
        ),
    ]
