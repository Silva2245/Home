# Generated by Django 5.1.2 on 2024-11-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('uname', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=100)),
            ],
        ),
    ]
