# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import kitbuilder.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomKit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('new', models.BooleanField(default=True)),
                ('on_sale', models.BooleanField(default=False)),
                ('soundcloud', models.CharField(max_length=200)),
                ('image', models.FileField(storage=kitbuilder.models.OverwriteStorage(), upload_to=kitbuilder.models.upload_kit_image)),
                ('rating', models.DecimalField(default=0, max_digits=5, decimal_places=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KitDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('selling_point1', models.TextField(blank=True)),
                ('selling_point2', models.TextField(blank=True)),
                ('selling_point3', models.TextField(blank=True)),
                ('author', models.CharField(max_length=50, blank=True)),
                ('date_created', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('percent_off', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('demo', models.FileField(storage=kitbuilder.models.OverwriteStorage(), upload_to=kitbuilder.models.upload_sample_demo)),
                ('wav', models.FileField(storage=kitbuilder.models.OverwriteStorage(), upload_to=kitbuilder.models.upload_sample)),
                ('type', models.CharField(max_length=2, choices=[(b'KD', b'Kick'), (b'SD', b'Snare'), (b'CP', b'Clap'), (b'PC', b'Percussion'), (b'FX', b'Sound FX'), (b'LO', b'Loop')])),
                ('kit', models.ForeignKey(to='kitbuilder.Kit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kit',
            name='description',
            field=models.ForeignKey(to='kitbuilder.KitDescription'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kit',
            name='price',
            field=models.ForeignKey(to='kitbuilder.Price'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kit',
            name='sale',
            field=models.ForeignKey(to='kitbuilder.Sale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kit',
            name='tags',
            field=models.ManyToManyField(to='kitbuilder.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customkit',
            name='samples',
            field=models.ManyToManyField(to='kitbuilder.Sample'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customkit',
            name='user',
            field=models.ForeignKey(to='userprofile.UserProfile'),
            preserve_default=True,
        ),
    ]
