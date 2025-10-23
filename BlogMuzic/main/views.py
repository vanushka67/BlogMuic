from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View
from .models import Post
from .models import  Photo

def index(request):
    return render(request, 'main/index.html')
# Create your views here.
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'main/post.html', {'post_list': posts})
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'main/photo_list.html', {'photos': photos})
