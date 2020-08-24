from rest_framework.test import APITestCase
from ..models import Student


class StudentViewTest(APITestCase):
    def test_should_render_view(self):
        student = Student.objects.create(
            name='keng',
            age=10
        )
        
        response = self.client.get('/student/')
        
        student_list = [
            {
                'name':'keng',
                'age':'10', 
                'gender': None,
            }
        ]
        
        assert response.data == student_list