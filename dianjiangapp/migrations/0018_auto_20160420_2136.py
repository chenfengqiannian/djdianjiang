# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0017_gongcheng_yaoqing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='reship',
            field=dianjiangapp.fields.Mymanytomany(to='dianjiangapp.user'),
        ),
    ]
