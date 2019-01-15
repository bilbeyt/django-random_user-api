from rest_framework import serializers
from api.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "last_name", "mobile_number"]


class StudentOtherSerializer(serializers.Serializer):
    name = serializers.CharField()
    last_name = serializers.CharField()
    mobile_number = serializers.IntegerField()
    
