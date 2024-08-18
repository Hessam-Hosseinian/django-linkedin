from django.utils import timezone

from django.shortcuts import render

from post.models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()
    posts = posts[::-1]
    authuser = request.user
    return render(request, 'home.html', {'posts': posts, 'authuser': authuser})
