# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0003_auto_20160412_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='touxiang',
            field=dianjiangapp.fields.ListField(),
        ),
    ]
