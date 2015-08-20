# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sample', '0002_auto_20150820_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='content_type',
            field=models.ForeignKey(default=None, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='sample',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
