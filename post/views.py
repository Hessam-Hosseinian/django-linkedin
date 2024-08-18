from django.utils import timezone

from django.shortcuts import render

from post.models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()
    posts = posts[::-1]
    datetime = timezone.now()
    print(datetime)
    authuser = request.user
    return render(request, 'home.html', {'posts': posts, 'datetime': datetime, 'authuser': authuser})
