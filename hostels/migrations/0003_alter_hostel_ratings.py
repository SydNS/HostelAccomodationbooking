# Generated by Django 4.0.1 on 2022-02-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0002_hostel_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='ratings',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
