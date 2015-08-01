# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progresstracker', '0003_team_webhook_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='team',
            field=models.ForeignKey(related_name='workers', to='progresstracker.Team'),
        ),
    ]
