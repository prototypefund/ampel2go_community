# Generated by Django 2.1.1 on 2020-03-12 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200312_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiArticle1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chapter_id', models.IntegerField(default=1)),
                ('subchapter_id', models.IntegerField(default=1)),
                ('title', models.CharField(default='title', max_length=100)),
                ('title_short', models.CharField(default='title_short', max_length=50)),
                ('body', models.TextField(default='body')),
                ('date', models.DateField(default=datetime.datetime(2020, 3, 12, 18, 34, 13, 427001))),
            ],
        ),
        migrations.DeleteModel(
            name='WikiArticle',
        ),
    ]
