from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts',PostViewSet)


urlpatterns = [

    path("posts/", PostView.as_view(), name="posts"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="post_delete"),
    path("api/", include(router.urls)),
    path("rest-api/", include('rest_framework.urls', namespace="rest_framework"))


]
