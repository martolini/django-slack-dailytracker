# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progresstracker', '0002_auto_20150721_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='webhook_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
