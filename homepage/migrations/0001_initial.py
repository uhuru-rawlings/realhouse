# Generated by Django 4.0.4 on 2022-05-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('bedrooms', models.IntegerField()),
                ('areaofland', models.IntegerField()),
                ('areaofhouse', models.IntegerField()),
                ('price', models.IntegerField()),
                ('interiorimage1', models.ImageField(upload_to='images')),
                ('interiorimage2', models.ImageField(upload_to='images')),
                ('exteriorimage', models.ImageField(upload_to='images')),
            ],
            options={
                'db_table': 'Houses',
            },
        ),
    ]
