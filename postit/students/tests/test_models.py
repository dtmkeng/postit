from django.test import TestCase
from ..models import Student, Gender


# Create your tests here.
class StudentModelTest(TestCase):
    fixtures = ['student','gender']
    # def test_should_create_model(self):
    #     name = 'new normal'
    #     age = 10
        
    #     #When
    #     gender = Gender.objects.create(gender='man')
    #     result = Student.objects.create(
    #         name=name,
    #         age=age,
    #         gender=gender,
    #     )

    #     #Then
    #     self.assertEqual(result.name, name)
    #     self.assertEqual(result.age, age)
    
    def test_create_student(self):
        
        s = Student.objects.get(pk=1)
        print(s)
        