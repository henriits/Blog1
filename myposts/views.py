from django.shortcuts import render

from myposts.models import Post
# Create your views here.
def home(request):
    recent_post = Post.objects.all().order_by("-created_date")

    return render(request, 'home.html', {'posts': recent_post})


def posts(request):
    post = Post.objects.all()
    return render(request, "posts.html",  {'posts': post})


