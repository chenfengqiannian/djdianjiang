# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0018_auto_20160420_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='reship',
            field=models.ManyToManyField(to='dianjiangapp.user'),
        ),
    ]
