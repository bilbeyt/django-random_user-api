from django.urls import path
from api import views


urlpatterns = [
    path("", views.StudentView.as_view(), name="student_api"),
    path("student/", views.StudentUi.as_view(), name="student")
]
