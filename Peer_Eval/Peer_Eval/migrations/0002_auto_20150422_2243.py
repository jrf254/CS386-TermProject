# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Peer_Eval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='enddate',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 6, 22, 43, 5, 826000)),
            preserve_default=True,
        ),
    ]
