# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0020_auto_20160421_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pingjia',
            field=models.FloatField(default=0.0, verbose_name=b'\xe8\xaf\x84\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='pingjiaxingji',
            field=models.FloatField(default=0.0, verbose_name='\u8bc4\u4ef7\u661f\u7ea7'),
        ),
    ]
