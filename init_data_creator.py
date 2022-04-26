import os
import random
import string
import types
import django
from django.db import connection, reset_queries

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectED.settings')
django.setup()
from django.db.models import Q
from django.contrib.auth.models import User, Group, Permission, make_password
from blog.models import PostModel, PostComment, PostCategory

name_list = ["Zharya", "Abraham", "Abram", "Oz", "Michael"]
category_list = ["Категория 1", "Еще один", "Тест.Кат", "Под.Каст"]


def create_user_group():
    group, flag = Group.objects.get_or_create(name="user")
    if flag:
        perm = Permission.objects.filter(Q(name__icontains="Комментарий") | Q(name__icontains="Статья"))
        group.permissions.set(perm)


def del_all():
    PostModel.objects.all().delete()
    PostCategory.objects.all().delete()
    User.objects.filter(username__in=name_list).delete()
    reset_queries()


def create_test_user():
    User.objects.bulk_create([
        User(
            username=name,
            email=f"{name}@pidr.net",
            password=make_password("123456"))
        for name in name_list
    ])


def add_user_to_group():
    Group.objects.get(name="user").user_set.set(
        User.objects.filter(username__in=name_list)
    )


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
    category_list_from_db = [i["pk"] for i in PostCategory.objects.all().values("pk")]
    author = [i["pk"] for i in User.objects.filter(is_superuser=False).values("pk")]

    PostModel.objects.bulk_create([
        PostModel(
            title=f"OS.{key}()",
            text=value.__doc__ if value.__doc__ else "empty",
            author_id=random.choice(author),
            category_id=random.choice(category_list_from_db)
        )
        for key, value in posts.items()
    ])


def create_comment():
    post_id = [i["pk"] for i in PostModel.objects.all().values("pk")]
    author = [i["pk"] for i in User.objects.filter(is_superuser=False).values("pk")]

    PostComment.objects.bulk_create([
        PostComment(
            text="".join([
                random.choice(list(string.ascii_letters) + [" ", ] * 10)
                for _ in range(random.randint(10, 100))
            ]),
            author_id=random.choice(author),
            post_id=random.choice(post_id)
        )
        for _ in range(100)
    ])


def main():
    del_all()
    create_user_group()
    create_test_user()
    add_user_to_group()
    create_category()
    create_posts()
    create_comment()


if __name__ == '__main__':
    main()
    print(*connection.queries, sep="\n")
