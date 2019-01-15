from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer, StudentOtherSerializer
from api.forms import TalentForm
from django.shortcuts import redirect
from django.views.generic.base import TemplateView


class StudentView(APIView):
    form_class = TalentForm

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        form = self.form_class(data=request.data)
        if not form.is_valid():
            raise ValueError("Invalid")
        serializer = StudentOtherSerializer(data=request.data)
        if serializer.is_valid():
            student = Student(**serializer.data)
            student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,                status=status.HTTP_400_BAD_REQUEST)


class StudentUi(TemplateView):
    template_name = "api/apifile.html"
    form_class = TalentForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("student")
        return super().dispatch(request, *args, **kwargs)

    def get_queyset(self):
        return Student.other_objects.filter(name__contains="mesut")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["test"] = self.get_queyset()
        context["form"] = self.form_class()
        return context