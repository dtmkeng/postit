from django.test import TestCase
from ..models import Post
import json


class PostViewsTest(TestCase):
    def test_should_have_render(self):
        responces = self.client.get('/post/')
        self.assertEqual(responces.status_code, 200)
        
    def test_should_have_return_result(self):
        caption = 'new normal'
        post_by = 'pm. jan'
        location = 'thai'
        
        post = Post.objects.create(
            caption = caption,
            post_by = post_by,
            location = location,
        )
        
        responces = self.client.get('/post/')
        
        self.assertEqual(responces.content.decode('utf-8'), json.dumps([{
            "caption":caption,
            "post_by":post_by,
            "location":location,
        }]))
        
    
    
