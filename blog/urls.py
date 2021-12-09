from django.urls import path
from .views import PostAllView, AddPost, PostOneView,AddComment, DelPost, UpdatePost

app_name = 'blog'
urlpatterns = [
    path("", PostAllView.as_view(), name="all_posts"),
    path("cat/<int:cat>/", PostAllView.as_view(), name="cat_posts"),
    path("detail/<int:pk>/", PostOneView.as_view(), name="detail"),
    path("add/", AddPost.as_view(), name="add_post"),
    path("add-comment/<int:post_id>/", AddComment.as_view(), name="add_comment"),
    path("del/<int:pk>/", DelPost.as_view(), name="del"),
    path("edit/<int:pk>/", UpdatePost.as_view(), name="edit")
]
