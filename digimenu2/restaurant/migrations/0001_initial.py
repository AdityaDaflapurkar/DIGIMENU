# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('cuisine_id', models.AutoField(serialize=False, primary_key=True)),
                ('cuisine_name', models.CharField(max_length=200)),
                ('image_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table', models.IntegerField()),
                ('menu_item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('orderid', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'Nochange', max_length=20, choices=[(b'Nochange', b'no change'), (b'Received', b'received'), (b'Preparing', b'preparing'), (b'Prepared', b'prepared'), (b'Delivered', b'delivered'), (b'Unavailable', b'unavailable')])),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_item', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image_path', models.CharField(max_length=100)),
                ('cuisine_id', models.ForeignKey(to='restaurant.Cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Usertable',
            fields=[
                ('table_no', models.IntegerField(serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
