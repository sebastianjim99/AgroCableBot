# Generated by Django 4.2.7 on 2024-01-12 15:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imacuna', '0005_rename_rol_roles_delete_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Usuarios',
        ),
    ]
