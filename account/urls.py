from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
]
