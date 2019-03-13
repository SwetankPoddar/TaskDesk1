# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-12 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskdesk', '0005_auto_20190312_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryImage',
            new_name='category_image',
        ),
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
