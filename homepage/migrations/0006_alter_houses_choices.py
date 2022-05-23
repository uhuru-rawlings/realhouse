# Generated by Django 4.0.4 on 2022-05-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_availability_houses_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='choices',
            field=models.CharField(choices=[('Single-Family Homes', 'Single-Family Homes'), ('Semi-Detached Home', 'Semi-Detached Home'), ('Multifamily Homes', 'Multifamily Homes'), ('Townhomes', 'Townhomes'), ('Apartments', 'Apartments'), ('Condominiums', 'Condominiums'), ('Co-Ops', 'Co-Ops'), ('Tiny Home ', 'Tiny Home '), ('Mobile Home', 'Mobile Home')], default='Townhomes', max_length=100),
        ),
    ]
