# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0021_auto_20160421_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pingjia',
            new_name='pingjiaxingji',
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.BooleanField(default=False, verbose_name='\u5de5\u5320or\u70b9\u5320,true,false'),
        ),
    ]
