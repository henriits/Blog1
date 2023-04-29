from django.shortcuts import render

from myposts.models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()

    return render(request, 'home.html', {'posts': post})


def posts(request):
    post = Post.objects.all()
    return render(request, "posts.html",  {'posts': post})
