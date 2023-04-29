from django.urls import path
from .views import *


urlpatterns = [
    path("",home, name="home"),
    path("posts/", posts, name="posts"),
    path("create/",CreateView.as_view(), name="product_create")
]
