from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import Login, Registration, AccountPageView

app_name = 'account'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('detail/<int:pk>/', AccountPageView.as_view(), name="account_detail"),
]
