# Generated by Django 2.1.5 on 2019-01-15 06:28

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_color'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('other_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
