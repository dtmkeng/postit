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
        
    def test_should_get_post_data_after_create(self):
        req = {
            "caption":'caption1',
            "post_by":'post_by',
            "location":'location',
        }
        req_json = json.dumps(req)
        responces = self.client.post('/post/', req_json, content_type='application/json')
        posts = Post.objects.all()

        assert responces.status_code == 200
        assert len(posts) == 1
        