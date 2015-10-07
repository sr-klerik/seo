# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_group', models.CharField(max_length=100)),
                ('url_group', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_text', models.TextField()),
                ('date_text', models.DateTimeField(verbose_name=b'date published')),
                ('likes', models.IntegerField(default=0)),
                ('reposts', models.IntegerField(default=0)),
                ('social_bound', models.CharField(max_length=10, choices=[(b'vk', b'vkontakte'), (b'fb', b'facebook'), (b'tw', b'twitter')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=200)),
                ('nickname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(default=b'Male', max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('avatar', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Social_VK',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='seouser.User')),
                ('login', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=100)),
                ('api_key', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='seouser.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(to='seouser.User'),
        ),
    ]
