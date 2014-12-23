# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0003_auto_20141222_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customkit',
            name='user',
            field=models.ForeignKey(related_name='custom_kits', to='userprofile.UserProfile'),
            preserve_default=True,
        ),
    ]
