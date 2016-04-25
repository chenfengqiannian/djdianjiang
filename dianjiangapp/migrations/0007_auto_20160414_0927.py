# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0006_auto_20160413_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='gongchengjindu',
            field=models.TextField(verbose_name='\u5de5\u7a0b\u8fdb\u5ea6', blank=True),
        ),
    ]
