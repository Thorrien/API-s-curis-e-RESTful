# Generated by Django 4.2 on 2024-06-28 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='can_be_shared',
            new_name='can_data_be_shared',
        ),
    ]
