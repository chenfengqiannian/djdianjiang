# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0019_auto_20160420_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='zhiding',
            field=dianjiangapp.fields.ListField(verbose_name='\u6307\u5b9a', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dizhi',
            field=models.CharField(max_length=255, verbose_name='\u5730\u5740', blank=True),
        ),
    ]
