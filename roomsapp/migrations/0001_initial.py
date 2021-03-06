# Generated by Django 4.0.1 on 2022-02-04 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roommodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
                ('photo', models.ImageField(upload_to='hostels_rooms/')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=8)),
                ('lavatory', models.CharField(choices=[('In Room', 'In Room'), ('Outdoors', 'Outdoors')], max_length=12)),
                ('room_capacity', models.CharField(choices=[('Double', 'Double'), ('Single', 'Single'), ('Triple', 'Triple')], max_length=10)),
                ('meal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('availbilitystatus', models.CharField(choices=[('Booked', 'Booked'), ('Vacant', 'Vacant'), ('Filled', 'Filled'), ('Half_full', 'Half_full')], max_length=10)),
                ('hostel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostels.hostel')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'db_table': 'rooms',
                'managed': True,
            },
        ),
    ]
