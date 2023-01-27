# Generated by Django 4.1.5 on 2023-01-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('MenuId', models.AutoField(primary_key=True, serialize=False)),
                ('MenuName', models.CharField(max_length=500)),
                ('plat', models.CharField(max_length=500)),
                ('DateOfCreation', models.DateField()),
                ('PhotoFile', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='plat',
            fields=[
                ('PlatId', models.AutoField(primary_key=True, serialize=False)),
                ('PlatNameName', models.CharField(max_length=500)),
            ],
        ),
    ]
