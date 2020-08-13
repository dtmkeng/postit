from django.test import TestCase
from ..models import Student
from ..serializer import StudentSerializer


# Create your tests here.
class StudentSerializerTest(TestCase):
    def test_should_serializer(self):
        student = Student.objects.create(
            name='keng',
            age=12,
        )
        students = Student.objects.all()
        
        serializer = StudentSerializer(student)
        
        expected =  {
                'name':'keng',
                'age':'12',
        }
        
        assert serializer.data == expected
        