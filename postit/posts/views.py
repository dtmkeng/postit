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
    
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            result = Post.objects.create(
                caption = data['caption'],
                post_by = data['post_by'],
                location = data['location'],
            )
            return HttpResponse(200)
        except expression:
            return HttpResponse(500)
        