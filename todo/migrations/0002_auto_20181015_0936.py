# Generated by Django 2.0.9 on 2018-10-15 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['deadline']},
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('normal', 'normal'), ('high', 'high')], default='normal', max_length=100),
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]
