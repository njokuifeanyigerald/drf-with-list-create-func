from re import I
from rest_framework import generics
from .serializer import StudentSerializeer 
from .models import Student
# from rest_framework.response import Response

class StudentApi(generics.ListCreateAPIView):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializeer