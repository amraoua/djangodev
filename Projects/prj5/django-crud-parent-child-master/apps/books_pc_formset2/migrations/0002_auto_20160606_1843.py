# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_pc_formset2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='contribution',
            field=models.IntegerField(choices=[(1, 'Author'), (2, 'EDITOR'), (3, 'REVIEWER')]),
        ),
    ]
