from os import environ as env

if not 'DJANGO_SETTINGS_MODULE' in env:
    from ProjectED import settings
    env.setdefault('DJANGO_SETTINGS_MODULE', settings.__name__)

import django
django.setup()


from django.db.models import Q

django.setup()

from django.contrib.auth.models import User, Group, Permission
from blog.models import PostModel, PostComment, PostCategory


def create_user_group():
    perm = Permission.objects.filter(Q(name__icontains="Комментарий") | Q(name__icontains="Статья"))
    user = Group(name="users")
    user.save()
    user.permissions.set(perm)


if __name__ == '__main__':
    create_user_group()