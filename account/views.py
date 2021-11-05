from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm, RegistrationForms
from ProjectED.utils import DataMixin


class Registration(CreateView, DataMixin):
    template_name = "registration/registration.html"
    form_class = RegistrationForms
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save(commit=False)
                user.save()
                user_group = Group.objects.get(name='user')
                user.groups.add(user_group)
                return redirect('login')
        else:
            print(form.__dict__)
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Регистрация")
        print(context)
        return context


class Login(LoginView, DataMixin):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Вход")
        return context
