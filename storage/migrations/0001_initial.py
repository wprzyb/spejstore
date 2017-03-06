# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django_hstore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('props', django_hstore.fields.DictionaryField()),
            ],
        ),
    ]