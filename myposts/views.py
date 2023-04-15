from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def posts(request):
    return render(request, "posts.html")
