from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import viewsets
from .forms import PostForm
from myposts.serializers import PostSerializer
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, FormView

# this library is used for debugging
import pdb


class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/posts.html'
    success_url = reverse_lazy('list_posts')
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset().filter(author=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return queryset


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

# class based views

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/create_post.html"
    fields = ["title", "text", "image","is_featured"]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    fields = ["title", "text", "image"]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts")


# REST API

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer