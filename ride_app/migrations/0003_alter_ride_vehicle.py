# Generated by Django 4.2.11 on 2024-04-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_app', '0002_ride_vehicle_alter_ride_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='vehicle',
            field=models.CharField(choices=[('ALL', 'all'), ('CAR', 'car'), ('BIKE', 'bike'), ('AUTO', 'auto')], max_length=30),
        ),
    ]
