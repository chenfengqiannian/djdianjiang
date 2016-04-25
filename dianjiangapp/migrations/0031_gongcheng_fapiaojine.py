# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0030_auto_20160424_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='fapiaojine',
            field=models.CharField(max_length=255, verbose_name='\u53d1\u7968\u91d1\u989d', blank=True),
        ),
    ]
