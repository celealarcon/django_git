# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('last_commit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'repo',
            },
        ),
        migrations.CreateModel(
            name='UpdateInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'updateinfo',
            },
        ),
    ]
