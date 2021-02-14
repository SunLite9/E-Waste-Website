# Generated by Django 3.1.3 on 2020-12-22 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_bookappointment_booked_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='pickupdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bookappointment',
            name='booked_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 17, 59, 16, 345758), null=True),
        ),
    ]
