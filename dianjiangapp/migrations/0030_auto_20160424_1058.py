# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0029_auto_20160423_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='jieshutime',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='kaishitime',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='gongcheng',
            name='reship',
            field=models.ManyToManyField(to='dianjiangapp.user', blank=True),
        ),
    ]
