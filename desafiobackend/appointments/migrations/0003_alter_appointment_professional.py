# Generated by Django 5.1.2 on 2024-10-30 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_initial'),
        ('users', '0002_alter_user_managers_remove_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users.professional'),
        ),
    ]
