# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_apple'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('item1', models.CharField(max_length=50, null=True)),
                ('qt1', models.IntegerField(default=1)),
                ('price1', models.BigIntegerField(default=0)),
                ('status1', models.CharField(default='not bought', max_length=20)),
                ('item2', models.CharField(max_length=50, null=True)),
                ('qt2', models.IntegerField(default=1)),
                ('price2', models.BigIntegerField(default=0)),
                ('status2', models.CharField(default='not bought', max_length=20)),
                ('item3', models.CharField(max_length=50, null=True)),
                ('qt3', models.IntegerField(default=1)),
                ('price3', models.BigIntegerField(default=0)),
                ('status3', models.CharField(default='not bought', max_length=20)),
                ('total', models.BigIntegerField(default=0)),
            ],
        ),
    ]
