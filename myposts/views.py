from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

#   from .forms import SignUpForm, PostForm  / post form is not required if used createpostposts/



from .models import Post
# Create your views here.
from django.contrib.auth.decorators import login_required

# These are for class based views
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, FormView

# this library is used for debugging
import pdb




class PostView(LoginRequiredMixin, ListView):
    """    def get(self,request):
        # filter posts to list only for login  users

        post = Post.objects.filter(author=request.user)
        return render(request, "posts.html", {'posts': post})"""

    model = Post
    template_name = 'posts/posts.html'
    success_url = reverse_lazy('posts')
    context_object_name = 'posts'

    def get_queryset(self):
        """This filters out other posts and only shows user posts!"""
        return super().get_queryset().filter(author=self.request.user).order_by("-created_date")


# class based views

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/create_post.html"
    fields = ["title", "text", ]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    fields = ["title", "text", ]
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts")


"""def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = SignUpForm()
        return render(request, "registration/signup.html", {'form': form})
"""

