# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_id', models.CharField(verbose_name='public_id', unique=True, max_length=12, editable=False, db_index=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, auto_now_add=True, null=True, verbose_name='last modified')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'created',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_id', models.CharField(verbose_name='public_id', unique=True, max_length=12, editable=False, db_index=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, auto_now_add=True, null=True, verbose_name='last modified')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'created',
            },
            bases=(models.Model,),
        ),
    ]
