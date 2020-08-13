from django.test import TestCase
from ..models import Student


# Create your tests here.
class StudentModelTest(TestCase):
    def test_should_create_model(self):
        name = 'new normal'
        age = 10
        
        #When
        result = Student.objects.create(
            name=name,
            age=age,
        )

        #Then
        self.assertEqual(result.name, name)
        self.assertEqual(result.age, age)
        