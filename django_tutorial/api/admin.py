from django.contrib import admin
from api.models import Student, StudentDetail, RandomUser


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "mobile_number"]
    list_filter = ["name"]
    search_fields = ("name",)


class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ["student_code", "data", "created_at"]
    search_fields = ["student_code", "data"]
    list_filter = ["student_code"]


class RandomUserAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "age", "mobile_number", "code"]
    search_fields = ["name", "last_name"]
    list_filter = ["age"]


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail, StudentDetailAdmin)
admin.site.register(RandomUser, RandomUserAdmin)