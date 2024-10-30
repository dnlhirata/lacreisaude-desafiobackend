# Generated by Django 5.1.2 on 2024-10-30 20:04

import users.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
