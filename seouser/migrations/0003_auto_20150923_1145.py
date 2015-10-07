# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seouser', '0002_auto_20150922_1728'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='SeoUser',
        ),
    ]
