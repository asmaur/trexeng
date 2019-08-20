from django.shortcuts import render, get_list_or_404
from .models import *
from django.conf import settings
# Create your views here.
def blog(request):
    posts = Post.objects.all().filter(publicar=True)
    return render(request, "blog/projeto.html", {"posts": posts, "base_url": settings.MEDIA_URL_PATCH})

def detail(request, code=None, slug=None):
    post = Post.objects.get(code=code)
    images = Image.objects.filter(post__code=code)
    return render(request, "blog/blog.html", {"post":post, "images": images, "base_url": settings.MEDIA_URL_PATCH})

def contato(request):
    return render(request, "blog/contato.html")
