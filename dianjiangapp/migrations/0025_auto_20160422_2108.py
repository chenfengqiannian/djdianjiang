# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0024_auto_20160422_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shezhi',
            name='neirong',
            field=models.TextField(verbose_name='\u5185\u5bb9', blank=True),
        ),
        migrations.AlterField(
            model_name='shezhi',
            name='tupian',
            field=models.ImageField(upload_to=b'images', max_length=255, verbose_name='\u8bbe\u7f6e\u56fe\u7247', blank=True),
        ),
    ]
