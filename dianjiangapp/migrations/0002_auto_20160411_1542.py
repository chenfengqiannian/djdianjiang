# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shouzhijilu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('neirong', models.CharField(max_length=255, verbose_name='\u5185\u5bb9')),
            ],
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='fapiaodizhi',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u5730\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='fapiaojisongshijian',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u5bc4\u9001\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='fapiaomingcheng',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='fapiaoshoujian',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u6536\u4ef6\u4eba', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='fapiaotaitou',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u62ac\u5934', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='fapiaoyouzheng',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u90ae\u653f\u7f16\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='pingjia',
            field=models.CharField(max_length=255, verbose_name='\u8bc4\u4ef7', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='yaoqiu',
            field=models.CharField(max_length=255, verbose_name='\u8981\u6c42', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='biaoqian',
            field=models.CharField(max_length=255, verbose_name='\u6807\u7b7e', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gongzhong',
            field=models.CharField(max_length=255, verbose_name='\u5de5\u79cd', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gongzuodi',
            field=models.CharField(max_length=255, verbose_name='\u5de5\u4f5c\u5730', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nichang',
            field=models.CharField(max_length=255, verbose_name='\u6635\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='xingming',
            field=models.CharField(max_length=255, verbose_name='\u59d3\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zhengshu',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name='\u8bc1\u4e66', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ziwojieshao',
            field=models.CharField(max_length=255, verbose_name='\u81ea\u6211\u4ecb\u7ecd', blank=True),
        ),
        migrations.AddField(
            model_name='shouzhijilu',
            name='suoshuid',
            field=models.ForeignKey(related_name='eq_xiaoxiid', to='dianjiangapp.user'),
        ),
    ]
