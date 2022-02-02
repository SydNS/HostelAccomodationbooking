# Generated by Django 4.0.1 on 2022-02-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/')),
                ('location', models.CharField(max_length=50)),
                ('total_rooms', models.IntegerField(default=0)),
                ('total_available_rooms', models.IntegerField(default=0)),
                ('total_booked_rooms', models.IntegerField(default=0)),
                ('singleroom_price', models.IntegerField(default=1500000)),
                ('doubleroom_price', models.IntegerField(default=2000000)),
            ],
        ),
    ]