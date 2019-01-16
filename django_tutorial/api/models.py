from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid
from itertools import islice


class StudentManager(models.Manager):
    def filter_student(self, name):
        return self.get_queryset().filter(name=name)


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField(null=True)
    other_objects = StudentManager()

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.name + "-" + self.last_name


class StudentDetail(models.Model):
    student_code = models.CharField(max_length=15)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student_detail"

    def __str__(self):
        return self.student_code

    
class Color(models.Model):
    RED = "RED"
    WHITE = "WHITE"
    BLUE = "BLUE"

    COLOR_CHOICES = (
        (RED, "RED"),
        (WHITE, "WHITE"),
        (BLUE, "BLUE"),
    )
    
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default=RED)


class RandomUserManager(models.Manager):
    def create_random_code(self):
        code = str(uuid.uuid4())[:20]
        if RandomUser.objects.filter(code=code).exists():
            return self.create_random_code()
        else:
            return code

    def save_data(self, list_data):
        for user in list_data:
            setattr(user, "code", self.create_random_code())
        self.bulk_create(list_data, 1000)


class RandomUser(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=30)
    age = models.IntegerField()
    code = models.CharField(max_length=20, unique=True)
    objects = RandomUserManager()

    def __str__(self):
        return self.name + " " + self.last_name
    