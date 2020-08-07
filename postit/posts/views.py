from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class PostView(View):
    def get(self, request):
        # html = '<div>Hello</div>'
        return render(request, 'post.html')
        