from django.contrib import admin
from django.test import TestCase
from ..models import Post
from ..admin import PostAdmin

class AdminConfigTest(TestCase):
    def test_is_should_register_pots(self):
        self.assertTrue(admin.site._registry[Post], PostAdmin)
    
    def test_is_should_set_list_display(self):
        expected = (
            'caption',
            'post_by',
            'location',
        )
        self.assertEqual(expected, PostAdmin.list_display)
        
    