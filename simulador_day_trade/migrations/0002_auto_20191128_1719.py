# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador_day_trade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacoes',
            name='corretagem',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=15, verbose_name='Corretagem*:'),
        ),
        migrations.AddField(
            model_name='operacoes',
            name='custos_b3',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=15, verbose_name='Custos B3*:'),
        ),
    ]
