# Generated by Django 4.1.5 on 2023-01-14 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='date_create',
            new_name='date_created',
        ),
    ]
