# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0004_auto_20141223_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kit',
            name='soundcloud',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
