# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0005_auto_20160413_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shezhi',
            name='tupian',
            field=models.ImageField(upload_to=b'images', max_length=255, verbose_name='\u8bbe\u7f6e\u56fe\u7247'),
        ),
    ]
