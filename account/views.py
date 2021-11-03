from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from ProjectED.utils import DataMixin


class Login(LoginView, DataMixin):
    template_name = "registration/login.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Вход")
        return context
