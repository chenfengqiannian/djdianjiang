# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0011_auto_20160420_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gongcheng',
            old_name='jieshushijian',
            new_name='jieshutime',
        ),
    ]
