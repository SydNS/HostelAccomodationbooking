# Generated by Django 4.0.1 on 2022-02-02 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roommodel',
            options={'managed': True, 'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
    ]