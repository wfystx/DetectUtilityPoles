# Generated by Django 2.1.3 on 2018-11-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
