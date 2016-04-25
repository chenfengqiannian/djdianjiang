# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0012_auto_20160420_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='pingjiaxingji',
            field=models.IntegerField(default=1, verbose_name='\u8bc4\u4ef7\u661f\u7ea7'),
        ),
    ]
