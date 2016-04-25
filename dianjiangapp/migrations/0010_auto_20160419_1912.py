# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0009_auto_20160414_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='autotime',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 11, 12, 45, 912000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rixin',
            field=models.IntegerField(default=0, verbose_name='\u65e5\u85aa'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='xinchou',
            field=models.IntegerField(default=0, verbose_name='\u85aa\u916c'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='zhuangtai',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(-2, '\u5220\u9664'), (-1, '\u5ba1\u6838\u5931\u8d25'), (0, '\u5ba1\u6838\u4e2d'), (1, '\u7b49\u5f85\u63a5'), (2, '\u5f85\u4ed8\u6b3e'), (3, '\u5f85\u7b7e\u5408\u540c'), (4, '\u6b63\u5728\u65bd\u5de5'), (5, '\u5de5\u7a0b\u5b8c\u6210\u5f85\u4ed8\u5c3e\u6b3e'), (6, '\u5b8c\u6210')]),
        ),
    ]
