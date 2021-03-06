# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('author', models.CharField(default='Jack', max_length=50)),
                ('text', models.TextField(default='')),
                ('publish_date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'DRAFT'), (2, 'POSTED'), (3, 'DELETED')])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Tag'),
        ),
    ]
