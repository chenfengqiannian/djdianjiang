# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0023_auto_20160422_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='biaoqian',
            field=models.CharField(max_length=255, verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
