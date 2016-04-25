# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0027_gongcheng_beizhu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='suozaidi',
            field=models.CharField(max_length=255, verbose_name='\u6240\u5728\u5730', blank=True),
        ),
    ]
