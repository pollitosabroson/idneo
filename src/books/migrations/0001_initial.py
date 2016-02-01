# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_id', models.CharField(verbose_name='public_id', unique=True, max_length=12, editable=False, db_index=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, auto_now_add=True, null=True, verbose_name='last modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('cover', models.ImageField(max_length=255, upload_to=books.models.get_upload_path, null=True, verbose_name='cover book', blank=True)),
                ('thumbnail', models.ImageField(max_length=255, upload_to=books.models.get_upload_thumbnail_path, null=True, verbose_name='cover book thumbnail', blank=True)),
                ('published_date', models.DateField(verbose_name='published date')),
                ('price', models.DecimalField(verbose_name='price', max_digits=6, decimal_places=2)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('archive', models.FileField(upload_to=books.models.get_upload_archive_path, max_length=255, verbose_name='archive')),
                ('category', models.ForeignKey(related_name='books', verbose_name='format', to='catalogs.Category')),
                ('format', models.ForeignKey(related_name='books', verbose_name='format', to='catalogs.Type')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'created',
            },
            bases=(models.Model,),
        ),
    ]
