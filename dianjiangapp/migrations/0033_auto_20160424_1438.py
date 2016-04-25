# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0032_auto_20160424_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='jieshutime',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='kaishitime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
