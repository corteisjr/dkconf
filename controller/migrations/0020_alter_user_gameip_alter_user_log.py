# Generated by Django 4.0.1 on 2022-10-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0019_enigma_solved_id_alter_enigma_solved_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='107.246.44.108', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-10-28 22:38:22.034846'),
        ),
    ]
