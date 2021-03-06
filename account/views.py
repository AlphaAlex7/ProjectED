from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from ProjectED.utils import DataMixin
from .forms import LoginForm, RegistrationForms
from blog.models import PostModel


class Registration(CreateView, DataMixin):
    template_name = "account/registration.html"
    form_class = RegistrationForms
    success_url = reverse_lazy('account:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save(commit=False)
                user.save()
                user_group = Group.objects.get(name='user')
                user.groups.add(user_group)
                return redirect('account:login')
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Регистрация")
        return context


class Login(LoginView, DataMixin):
    template_name = "account/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Вход")
        return context


class AccountPageView(DetailView, DataMixin):
    model = User
    template_name = "account/user_detail.html"
    context_object_name = "account_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Моя страница")
        context["account_posts_count"] = PostModel.objects.filter(author__id=self.object.id).count()
        context['account_detail__dict'] = context["account_detail"].__dict__
        print(context)
        return context
