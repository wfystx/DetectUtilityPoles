# Generated by Django 2.1.3 on 2018-12-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_nov6', '0002_auto_20181109_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='poles')),
            ],
        ),
    ]