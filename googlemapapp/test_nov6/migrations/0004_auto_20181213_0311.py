# Generated by Django 2.1.3 on 2018-12-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_nov6', '0003_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('time', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('lat', models.CharField(max_length=24)),
                ('lng', models.CharField(max_length=24)),
            ],
        ),
        migrations.DeleteModel(
            name='Pictures',
        ),
    ]
