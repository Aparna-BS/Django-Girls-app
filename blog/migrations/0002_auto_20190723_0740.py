# Generated by Django 2.2.2 on 2019-07-23 02:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 2, 10, 42, 611284, tzinfo=utc)),
        ),
    ]
