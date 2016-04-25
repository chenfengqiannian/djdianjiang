# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0007_auto_20160414_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shouzhijilu',
            name='suoshuid',
            field=models.ForeignKey(to='dianjiangapp.user'),
        ),
    ]
