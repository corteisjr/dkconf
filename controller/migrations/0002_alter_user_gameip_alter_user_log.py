# Generated by Django 4.0.1 on 2022-10-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='14.85.154.39', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-10-22 04:37:23.401964'),
        ),
    ]
