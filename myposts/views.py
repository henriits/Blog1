from django.shortcuts import render

from myposts.models import Post
# Create your views here.
from django.contrib.auth.decorators import login_required

# this library is used for debugging
import pdb

def home(request):
    recent_post = Post.objects.all().order_by("-created_date")

    return render(request, 'home.html', {'posts': recent_post})




# decorator for only authenticated user

@login_required()
def posts(request):
    # filter posts to list only for login  users

    post = Post.objects.filter(author=request.user)
    return render(request, "posts.html",  {'posts': post})


