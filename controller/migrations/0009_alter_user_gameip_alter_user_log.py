# Generated by Django 4.0.1 on 2022-10-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0008_alter_user_gameip_alter_user_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='148.180.144.152', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-10-26 23:51:03.477266'),
        ),
    ]