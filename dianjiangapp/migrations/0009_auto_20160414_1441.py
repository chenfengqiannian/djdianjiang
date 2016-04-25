# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dianjiangapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0008_auto_20160414_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shouzhijilu',
            name='suoshuid',
        ),
        migrations.AddField(
            model_name='user',
            name='shouzhijilu',
            field=dianjiangapp.fields.ListField(verbose_name='\u6536\u652f\u8bb0\u5f55', blank=True),
        ),
        migrations.DeleteModel(
            name='shouzhijilu',
        ),
    ]
