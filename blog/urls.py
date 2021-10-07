from django.urls import path
from .views import PostAllView, AddPost, PostOneView

urlpatterns = [
    path("", PostAllView.as_view()),
    path("detail/<int:pk>/", PostOneView.as_view(), name="detail"),
    path("add/", AddPost.as_view(), name="add_post")
]
