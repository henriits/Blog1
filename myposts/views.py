from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from myposts.models import Post
# Create your views here.
from django.contrib.auth.decorators import login_required

# These are for class based views
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View

# this library is used for debugging
import pdb


#def home(request):


class HomeView(View):
    def get(self,request):
        recent_post = Post.objects.all().order_by("-created_date")

        return render(request, 'home.html', {'posts': recent_post})
# decorator for only authenticated user

class PostView(LoginRequiredMixin,ListView):
    """    def get(self,request):
        # filter posts to list only for login  users

        post = Post.objects.filter(author=request.user)
        return render(request, "posts.html", {'posts': post})"""

    model = Post
    template_name = 'posts.html'
    success_url = reverse_lazy('posts')
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


# class based views

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ["title", "text", ]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["title", "text", ]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts")
