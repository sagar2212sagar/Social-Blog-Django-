# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-30 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_posts_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='favourite',
            new_name='favorite',
        ),
    ]