# Generated by Django 4.0.1 on 2022-01-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roommodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=8)),
                ('room_capacity', models.CharField(choices=[('Double', 'Double'), ('Single', 'Single'), ('Triple', 'Triple')], max_length=10)),
                ('meal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('rentfee', models.IntegerField(max_length=10)),
                ('availbilitystatus', models.CharField(choices=[('Booked', 'Booked'), ('Vacant', 'Vacant'), ('Filled', 'Filled'), ('Half_full', 'Half_full')], max_length=10)),
            ],
            options={
                'db_table': 'rooms',
                'managed': True,
            },
        ),
    ]