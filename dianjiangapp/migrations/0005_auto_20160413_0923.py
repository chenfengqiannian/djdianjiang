# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0004_auto_20160412_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gongcheng',
            name='fukuanfangshi',
        ),
        migrations.AddField(
            model_name='gongcheng',
            name='reship',
            field=models.ManyToManyField(to='dianjiangapp.user'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='pingjiatu',
            field=dianjiangapp.fields.ListField(verbose_name='\u8bc4\u4ef7\u56fe', blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='tupian',
            field=dianjiangapp.fields.ListField(verbose_name='\u56fe', blank=True),
        ),
        migrations.AlterField(
            model_name='shezhi',
            name='tupian',
            field=dianjiangapp.fields.ListField(verbose_name='\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='shouzhijilu',
            name='suoshuid',
            field=models.ForeignKey(related_name='eq_shouzhijiluid', to='dianjiangapp.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dengji',
            field=models.IntegerField(default=0, verbose_name='\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='jingyanzhi',
            field=models.IntegerField(default=0, verbose_name='\u7ecf\u9a8c\u503c'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shenfengzheng',
            field=dianjiangapp.fields.ListField(verbose_name='\u8eab\u4efd\u8bc1', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='touxiang',
            field=dianjiangapp.fields.ListField(verbose_name='\u5934\u50cf', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zhengshu',
            field=dianjiangapp.fields.ListField(verbose_name='\u8bc1\u4e66', blank=True),
        ),
    ]
