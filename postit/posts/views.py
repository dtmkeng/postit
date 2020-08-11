import json
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
class PostView(View):
    def get(self, request):
        # html = '<div>Hello</div>'
        # return render(request, 'post.html')
        
        posts = Post.objects.all()
        post_list = []
        for post in posts:
            res = {
                'caption': post.caption,
                'post_by': post.post_by,
                'location': post.location,
            }
            post_list.append(res)
        
        return HttpResponse(json.dumps(post_list), content_type='application/json') 
        