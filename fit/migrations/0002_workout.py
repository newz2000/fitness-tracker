# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-07 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.DurationField(default=1)),
                ('distance', models.DecimalField(blank=True, decimal_places=2, default=1.0, max_digits=5, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit.ExerciseTypes')),
            ],
        ),
    ]