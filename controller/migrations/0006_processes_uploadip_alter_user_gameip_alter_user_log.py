# Generated by Django 4.0.1 on 2022-10-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0005_processes_softupload_alter_lastip_ip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='processes',
            name='uploadip',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='17.219.122.30', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-10-26 15:27:23.853941'),
        ),
    ]
