# Generated by Django 4.0.1 on 2022-10-28 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0015_enigma_solved_alter_user_gameip_alter_user_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='145.155.40.99', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-10-28 17:50:18.492641'),
        ),
        migrations.CreateModel(
            name='enigma_solved',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('enigma', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='controller.enigma')),
            ],
        ),
    ]
