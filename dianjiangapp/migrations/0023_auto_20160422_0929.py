# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0022_auto_20160421_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='biaoqian',
            field=dianjiangapp.fields.ListField(verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
