# Generated by Django 3.1.3 on 2020-12-22 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20201221_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='pickuptime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bookappointment',
            name='booked_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 18, 6, 6, 893172), null=True),
        ),
    ]
