# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('exam_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('examname', models.TextField()),
                ('topicid', models.CharField(max_length=32)),
                ('groupid', models.CharField(max_length=32)),
                ('begintime', models.CharField(max_length=30)),
                ('endtime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='examinee',
            fields=[
                ('userid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('ticketnumber', models.CharField(max_length=30)),
                ('idcard', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=1000)),
                ('actstatus', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='examineegroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.CharField(max_length=32)),
                ('userid', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='examlib',
            fields=[
                ('examlib_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('options', models.CharField(max_length=4000)),
                ('anser', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=50)),
                ('createtime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='groupinfo',
            fields=[
                ('groupinfo_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('groupname', models.CharField(max_length=255)),
                ('createtime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='records',
            fields=[
                ('records_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('examid', models.CharField(max_length=32)),
                ('weigth', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=30)),
                ('Type', models.CharField(max_length=50)),
                ('sort', models.CharField(max_length=255)),
                ('testid', models.CharField(max_length=32)),
                ('title', models.TextField()),
                ('options', models.CharField(max_length=4000)),
                ('anser', models.CharField(max_length=100)),
                ('myanser', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='records_copy',
            fields=[
                ('records_copy_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('examid', models.CharField(max_length=32)),
                ('weigth', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=30)),
                ('Type', models.CharField(max_length=50)),
                ('sort', models.CharField(max_length=255)),
                ('testid', models.CharField(max_length=32)),
                ('title', models.TextField()),
                ('options', models.CharField(max_length=4000)),
                ('anser', models.CharField(max_length=100)),
                ('myanser', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='topics',
            fields=[
                ('topics_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('singlenumber', models.CharField(max_length=50)),
                ('singleweight', models.CharField(max_length=50)),
                ('multiplenumber', models.CharField(max_length=50)),
                ('multipleweight', models.CharField(max_length=50)),
                ('judgenumber', models.CharField(max_length=50)),
                ('judgeweight', models.CharField(max_length=50)),
                ('tiankongnumber', models.CharField(max_length=50)),
                ('tiankongweight', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='totalscores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalscores_id', models.CharField(max_length=32)),
                ('examid', models.CharField(max_length=32)),
                ('userid', models.CharField(max_length=32)),
                ('score', models.CharField(max_length=50)),
                ('createtime', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
