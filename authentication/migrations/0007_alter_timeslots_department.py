# Generated by Django 5.0.4 on 2024-05-12 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_timeslots_timeslotsperday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslots',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.department'),
        ),
    ]
