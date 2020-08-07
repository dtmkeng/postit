from django.views import View
from django.http import HttpResponse

# Create your views here.
class PostView(View):
    def get(self, request):
        html = '<div>Hello</div>'
        return HttpResponse(html)
        