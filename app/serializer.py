from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializeer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
