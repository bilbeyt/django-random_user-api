# Generated by Django 2.1.5 on 2019-01-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_studentdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('RED', 'RED'), ('WHITE', 'WHITE'), ('BLUE', 'BLUE')], default='RED', max_length=10)),
            ],
        ),
    ]
