# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progresstracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='slack_id',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='slack_id',
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='id',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
