# Generated by Django 4.0.1 on 2022-02-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0003_alter_hostel_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='number_of_doublerooms',
            field=models.IntegerField(default=2000000),
        ),
        migrations.AddField(
            model_name='hostel',
            name='number_of_singlerooms',
            field=models.IntegerField(default=1500000),
        ),
    ]
