import os
import random
import string
import types
import django
from django.db.transaction import atomic
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectED.settings')
django.setup()

from django.db.models import Q
from django.contrib.auth.models import User, Group, Permission
from blog.models import PostModel, PostComment, PostCategory

name_list = ["Zharya", "Abraham", "Abram", "Oz", "Michael"]
category_list = ["Категория 1", "Еще один", "Тест.Кат", "Под.Каст"]


def create_user_group():
    perm = Permission.objects.filter(Q(name__icontains="Комментарий") | Q(name__icontains="Статья"))
    user_group = Group(name="user")
    user_group.save()
    user_group.permissions.set(perm)


def del_test_users():
    User.objects.filter(username__in=name_list).delete()


def create_test_user():
    user_group = Group.objects.get(name="user")

    users = [
        User.objects.create_user(
            username=name,
            email=f"{name}@pidr.net",
            password="123456789").groups.set((user_group,))
        for name in name_list]
    return users


def create_category():
    PostCategory.objects.bulk_create(
        [PostCategory(title=title) for title in category_list]
    )


def create_posts():
    posts = {
        k: v
        for k, v in os.__dict__.items()
        if isinstance(v, types.FunctionType) and "_" not in k
    }
    category_list = [i["pk"] for i in PostCategory.objects.all().values("pk")]
    author = [i["pk"] for i in User.objects.filter(is_superuser=False).values("pk")]

    PostModel.objects.bulk_create([
        PostModel(
            title=f"OS.{key}()",
            text=value.__doc__ if value.__doc__ else "empty",
            author_id=random.choice(author),
            category_id=random.choice(category_list)
        )
        for key, value in posts.items()
    ])

def create_comment():
    post_id = [i["pk"] for i in PostModel.objects.all().values("pk")]
    author = [i["pk"] for i in User.objects.filter(is_superuser=False).values("pk")]

    PostComment.objects.bulk_create([
        PostComment(
            text="".join([random.choice(list(string.ascii_letters)+[" ",]*10) for _ in range(random.randint(10,100))]),
            author_id=random.choice(author),
            post_id=random.choice(post_id)
        ) for _ in range(100)
    ])

if __name__ == '__main__':
    create_user_group()
    # del_test_users()
    create_test_user()
    create_category()
    create_posts()
    create_comment()
    print(*connection.queries, sep="\n")
    print(sum([float(i["time"]) for i in connection.queries]))
    pass
