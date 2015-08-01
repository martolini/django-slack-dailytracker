# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progresstracker', '0004_auto_20150731_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='channel',
            field=models.CharField(default='dailyupdates', max_length=30),
            preserve_default=False,
        ),
    ]
