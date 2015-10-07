# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seouser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='social_bound',
            field=models.CharField(default=b'vkontakte', max_length=10, choices=[(b'vk', b'vkontakte'), (b'fb', b'facebook'), (b'tw', b'twitter')]),
        ),
    ]
