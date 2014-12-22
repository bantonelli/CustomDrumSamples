# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0002_auto_20141222_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='kit',
            field=models.ForeignKey(related_name='samples', to='kitbuilder.Kit'),
            preserve_default=True,
        ),
    ]
