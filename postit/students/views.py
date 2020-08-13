from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student

# Create your views here.
class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
        
        
    