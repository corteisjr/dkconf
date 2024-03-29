# Generated by Django 4.0.1 on 2022-10-25 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0002_alter_user_gameip_alter_user_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastIp',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ip', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='216.189.52.130', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-10-25 01:04:26.066638'),
        ),
    ]
