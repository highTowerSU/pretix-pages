# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 14:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import pretix.base.i18n


class Migration(migrations.Migration):

    dependencies = [
        ('pretix_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='require_confirmation',
            field=models.BooleanField(default=False, verbose_name='Require the user to acknowledge this page before an order is created (e.g. for terms of service).'),
        ),
        migrations.AlterField(
            model_name='page',
            name='link_in_footer',
            field=models.BooleanField(default=False, verbose_name='Show link in the event footer'),
        ),
        migrations.AlterField(
            model_name='page',
            name='link_on_frontpage',
            field=models.BooleanField(default=False, verbose_name='Show link on the event start page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(db_index=True, max_length=150, validators=[django.core.validators.RegexValidator(message='The slug may only contain letters, numbers, dots and dashes.', regex='^[a-zA-Z0-9.-]+$')], verbose_name='URL form'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=pretix.base.i18n.I18nTextField(verbose_name='Page content'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=pretix.base.i18n.I18nCharField(verbose_name='Page title'),
        ),
    ]
