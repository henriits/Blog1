from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="post_delete")
]
