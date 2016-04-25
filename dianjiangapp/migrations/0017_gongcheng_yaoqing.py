# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0016_auto_20160420_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='yaoqing',
            field=dianjiangapp.fields.ListField(verbose_name='\u9080\u8bf7\u5217\u8868', blank=True),
        ),
    ]
