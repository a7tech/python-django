# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('featured_image', models.FileField(upload_to=b'images')),
                ('movie_length', models.PositiveSmallIntegerField()),
                ('movie_release_date', models.DateTimeField()),
            ],
        ),
    ]
