# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0002_auto_20160411_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='pingjiatu',
            field=models.CharField(max_length=255, verbose_name='\u8bc4\u4ef7\u56fe'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='tupian',
            field=models.CharField(max_length=255, verbose_name='\u56fe'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='zhuangtai',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(-1, '\u5220\u9664'), (0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u5931\u8d25'), (1, '\u7b49\u5f85\u63a5'), (2, '\u5f85\u4ed8\u6b3e'), (3, '\u5f85\u7b7e\u5408\u540c'), (4, '\u6b63\u5728\u65bd\u5de5'), (5, '\u5de5\u7a0b\u5b8c\u6210\u5f85\u4ed8\u5c3e\u6b3e'), (6, '\u5b8c\u6210')]),
        ),
        migrations.AlterField(
            model_name='shezhi',
            name='tupian',
            field=models.CharField(max_length=255, verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shenfengzheng',
            field=models.CharField(max_length=255, verbose_name='\u8eab\u4efd\u8bc1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='touxiang',
            field=models.CharField(max_length=255, verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='user',
            name='zhengshu',
            field=models.CharField(max_length=255, verbose_name='\u8bc1\u4e66', blank=True),
        ),
    ]
