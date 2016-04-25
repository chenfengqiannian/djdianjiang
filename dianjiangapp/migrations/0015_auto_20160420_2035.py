# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dianjiangapp', '0014_user_gongsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gongcheng',
            name='zhuangtai',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(-2, '\u5220\u9664'), (-1, '\u5ba1\u6838\u5931\u8d25'), (0, '\u5ba1\u6838\u4e2d'), (1, '\u5f85\u7b7e\u5408\u540c'), (2, '\u5f85\u4ed8\u6b3e'), (3, '\u62db\u6807\u4e2d'), (4, '\u6b63\u5728\u65bd\u5de5'), (5, '\u5de5\u7a0b\u5b8c\u6210\u5f85\u4ed8\u5c3e\u6b3e'), (6, '\u5b8c\u6210')]),
        ),
    ]
