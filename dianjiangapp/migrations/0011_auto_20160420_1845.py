# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0010_auto_20160419_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='jieshushijian',
            field=models.DateField(default=datetime.datetime(2016, 4, 20, 18, 45, 40, 916000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gongcheng',
            name='kaishitime',
            field=models.DateField(default=datetime.datetime(2016, 4, 20, 18, 45, 46, 55000)),
            preserve_default=False,
        ),
    ]
