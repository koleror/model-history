# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_auto_20150820_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='object_id',
        ),
    ]
