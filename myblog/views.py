from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from myposts.forms import SignUpForm
from myposts.models import Post
from django.http import HttpResponse
from django.shortcuts import render
from myposts.models import Post


def home(request):
    featured_post = Post.objects.filter(is_featured=True)
    recent_posts = Post.objects.all().order_by('-created_date')
    return render(request, 'home.html', {'posts': recent_posts, 'featured_post': featured_post})

def about(request):
    return render(request, 'about.html')



class UserCreateView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
