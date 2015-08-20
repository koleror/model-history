# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('model_history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyentry',
            name='content_type',
            field=models.ForeignKey(default=None, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='historyentry',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
