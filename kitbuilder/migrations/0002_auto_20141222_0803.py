# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kit',
            old_name='rating',
            new_name='user_rating',
        ),
    ]
