# Generated by Django 2.1.5 on 2019-01-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_randomuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomuser',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
