from django.shortcuts import render
from django.urls import reverse_lazy

from myposts.models import Post
# Create your views here.
from django.contrib.auth.decorators import login_required

#These are for class based views
from django.views.generic import CreateView,ListView,UpdateView,DeleteView



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


# class based views

class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ["title","text",]
    success_url = reverse_lazy("posts")


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)