# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-03 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=50)),
                ('no_of_players', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='person',
            field=models.ManyToManyField(blank=True, null=True, to='manytomanyapp.Person'),
        ),
    ]
