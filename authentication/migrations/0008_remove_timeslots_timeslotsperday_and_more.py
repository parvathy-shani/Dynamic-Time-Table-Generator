# Generated by Django 5.0.4 on 2024-05-13 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_timeslots_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='TimeslotsPerDay',
        ),
        migrations.RemoveField(
            model_name='timeslots',
            name='daysPerWeek',
        ),
    ]