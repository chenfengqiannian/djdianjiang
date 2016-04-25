# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0026_user_shenfengzhengid'),
    ]

    operations = [
        migrations.AddField(
            model_name='gongcheng',
            name='beizhu',
            field=models.CharField(max_length=255, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
