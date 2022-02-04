# Generated by Django 4.0.1 on 2022-02-04 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roomsapp', '0001_initial'),
        ('useraccounts', '0001_initial'),
        ('hostels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookhosteltable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(choices=[('1 SEMESTER', '1 SEMESTER'), ('2 SEMESTER', '2 SEMESTER')], max_length=10)),
                ('arrival_date', models.DateField(blank=True, null=True)),
                ('payment_status', models.CharField(choices=[('PAID', 'PAID'), ('DUE', 'DUE')], max_length=10)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.student')),
                ('hostel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostels.hostel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomsapp.roommodel')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
                'db_table': 'bookhostel_table',
                'managed': True,
            },
        ),
    ]
