# Generated by Django 4.0.1 on 2022-02-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookhosteltable',
            name='booked',
        ),
        migrations.AlterField(
            model_name='bookhosteltable',
            name='duration',
            field=models.CharField(choices=[('1 SEMESTER', '1 SEMESTER'), ('2 SEMESTER', '2 SEMESTER')], max_length=10),
        ),
    ]