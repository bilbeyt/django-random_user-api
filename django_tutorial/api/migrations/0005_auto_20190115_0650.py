# Generated by Django 2.1.5 on 2019-01-15 06:50

from django.db import migrations


def test_migration(apps, schema_editor):
    student = apps.get_model("api", "Student")
    all_students = student.other_objects.all()
    all_students.update(mobile_number="123456789")


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190115_0628'),
    ]

    operations = [
        migrations.RunPython(test_migration)
    ]
