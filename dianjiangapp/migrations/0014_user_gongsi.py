# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0013_gongcheng_pingjiaxingji'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gongsi',
            field=models.CharField(max_length=255, verbose_name='\u516c\u53f8', blank=True),
        ),
    ]
