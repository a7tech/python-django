# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import movies.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 30, 16, 53, 26, 818807, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='featured_image',
            field=models.FileField(upload_to=b'images', validators=[movies.models.ImageValidator]),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_release_date',
            field=models.DateField(),
        ),
    ]
