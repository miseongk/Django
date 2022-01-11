from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_url_kwarg = 'student_pk' 
