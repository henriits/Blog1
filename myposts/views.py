from django.shortcuts import render

from myposts.models import Post
# Create your views here.
from django.contrib.auth.decorators import login_required
def home(request):
    recent_post = Post.objects.all().order_by("-created_date")

    return render(request, 'home.html', {'posts': recent_post})




@login_required()
def posts(request):
    post = Post.objects.all()
    return render(request, "posts.html",  {'posts': post})


