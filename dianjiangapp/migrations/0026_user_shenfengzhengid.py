# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0025_auto_20160422_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shenfengzhengid',
            field=models.CharField(max_length=255, verbose_name='\u8eab\u4efd\u8bc1', blank=True),
        ),
    ]
