# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0028_auto_20160423_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='biaoti',
            field=models.CharField(max_length=255, verbose_name='\u6807\u9898', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='gongzhong',
            field=models.CharField(max_length=255, verbose_name='\u5de5\u79cd', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='miaoshu',
            field=models.CharField(max_length=255, verbose_name='\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='xiangxidizhi',
            field=models.CharField(max_length=255, verbose_name='\u8be6\u7ec6\u5730\u5740', blank=True),
        ),
    ]
