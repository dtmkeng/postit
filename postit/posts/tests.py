from django.test import TestCase
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def test_is_shoud_instance_of_post(self): 
        self.assertEqual(isinstance(Post.objects.create(), Post), True)
        
    def test_is_should_create_post_model(self):
        #Give
        caption = 'new normal'
        post_by = 'pm. jan'
        location = 'thai'
        
        #When
        result = Post.objects.create(
            caption = caption,
            post_by = post_by,
            location = location,
        )

        #Then
        self.assertEqual(result.caption, caption)
        self.assertEqual(result.post_by, post_by)
        self.assertEqual(result.location, location)
