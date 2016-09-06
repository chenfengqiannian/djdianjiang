# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0033_auto_20160424_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='zhaobiao',
            field=dianjiangapp.fields.ListField(verbose_name='\u62db\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tixianshenqing',
            field=models.BooleanField(default=False, verbose_name='\u63d0\u73b0\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='zhiding',
            field=dianjiangapp.fields.ListField(verbose_name='\u5de5\u5320', blank=True),
        ),
    ]
