# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gongcheng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biaoti', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
                ('miaoshu', models.CharField(max_length=255, verbose_name='\u63cf\u8ff0')),
                ('suozaidi', models.CharField(max_length=255, verbose_name='\u6240\u5728\u5730')),
                ('xiangxidizhi', models.CharField(max_length=255, verbose_name='\u8be6\u7ec6\u5730\u5740')),
                ('tupian', models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u56fe')),
                ('gongzhong', models.CharField(max_length=255, verbose_name='\u5de5\u79cd')),
                ('yaoqiu', models.CharField(max_length=255, verbose_name='\u8981\u6c42')),
                ('xinchou', models.CharField(max_length=255, verbose_name='\u85aa\u916c')),
                ('fukuanfangshi', models.CharField(max_length=255, verbose_name='\u4ed8\u6b3e\u65b9\u5f0f')),
                ('zhuangtai', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u5931\u8d25'), (1, '\u7b49\u5f85\u63a5'), (2, '\u5f85\u4ed8\u6b3e'), (3, '\u5f85\u7b7e\u5408\u540c'), (4, '\u6b63\u5728\u65bd\u5de5'), (5, '\u5de5\u7a0b\u5b8c\u6210\u5f85\u4ed8\u5c3e\u6b3e'), (6, '\u5b8c\u6210')])),
                ('gongchengjindu', models.TextField(verbose_name='\u5de5\u7a0b\u8fdb\u5ea6')),
                ('pingjia', models.CharField(max_length=255, verbose_name='\u8bc4\u4ef7')),
                ('pingjiatu', models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u8bc4\u4ef7\u56fe')),
                ('fapiaomingcheng', models.CharField(max_length=255, verbose_name='\u53d1\u7968\u540d\u79f0')),
                ('fapiaotaitou', models.CharField(max_length=255, verbose_name='\u53d1\u7968\u62ac\u5934')),
                ('fapiaoyouzheng', models.CharField(max_length=255, verbose_name='\u53d1\u7968\u90ae\u653f\u7f16\u7801')),
                ('fapiaoshoujian', models.CharField(max_length=255, verbose_name='\u53d1\u7968\u6536\u4ef6\u4eba')),
                ('fapiaodizhi', models.CharField(max_length=255, verbose_name='\u53d1\u7968\u5730\u5740')),
                ('fapiaojisongshijian', models.CharField(max_length=255, verbose_name='\u53d1\u7968\u5bc4\u9001\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='shezhi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('neirong', models.CharField(max_length=255, verbose_name='\u5185\u5bb9')),
                ('tupian', models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u56fe\u7247')),
            ],
        ),
        migrations.CreateModel(
            name='tupianclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tupianshuju', models.ImageField(max_length=255, upload_to=b'images')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255, verbose_name='\u624b\u673a')),
                ('userpw', models.CharField(max_length=255, verbose_name='\u5bc6\u7801')),
                ('job', models.BooleanField(default=False, verbose_name='\u5de5\u5320or\u70b9\u5320')),
                ('didianchar', models.CharField(max_length=255, verbose_name='\u5730\u70b9')),
                ('touxiang', models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u5934\u50cf')),
                ('nichang', models.CharField(max_length=255, verbose_name='\u6635\u79f0')),
                ('zhifubaozhanghao', models.CharField(max_length=255, verbose_name='\u652f\u4ed8\u5b9d\u8d26\u53f7', blank=True)),
                ('zhanghuyue', models.FloatField(default=0.0, verbose_name='\u8d26\u6237\u4f59\u989d')),
                ('shenfengzheng', models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u8eab\u4efd\u8bc1')),
                ('xingming', models.CharField(max_length=255, verbose_name='\u59d3\u540d')),
                ('gongzhong', models.CharField(max_length=255, verbose_name='\u5de5\u79cd')),
                ('gongzuodi', models.CharField(max_length=255, verbose_name='\u5de5\u4f5c\u5730')),
                ('biaoqian', models.CharField(max_length=255, verbose_name='\u6807\u7b7e')),
                ('ziwojieshao', models.CharField(max_length=255, verbose_name='\u81ea\u6211\u4ecb\u7ecd')),
                ('zhengshu', models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u8bc1\u4e66')),
                ('dengji', models.IntegerField(verbose_name='\u7b49\u7ea7')),
                ('jingyanzhi', models.IntegerField(verbose_name='\u7ecf\u9a8c\u503c')),
            ],
        ),
    ]
