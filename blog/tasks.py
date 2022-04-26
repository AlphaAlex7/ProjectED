import time

from celery import shared_task
from django.core.mail import send_mail
from django.db.models import Count
import random
from ProjectED import settings
from ProjectED.celery_init import app
from .models import PostComment, PostModel, PostCategory
from django.contrib.auth.models import User
from random import choice
import string
import datetime


@app.task
def create_new_comment(post_id):
    text_comment = f"test celery {datetime.datetime.now()}" + "".join([choice(string.ascii_letters) for _ in range(50)])
    time.sleep(10)
    new_com = PostComment(post_id=post_id,
                          author=choice(User.objects.all()),
                          text=text_comment).save()
    return new_com


@app.task
def send_stat_for_me():
    count_all_post = PostModel.objects.all().count()
    count_all_comment = PostComment.objects.all().count()

    user_stat = User.objects.values("username").annotate(
        posts=Count("author", distinct=True),
        comment=Count("author_comment", distinct=True)
    )

    send_string = f"Всего постов: {count_all_post}, Всего комментариев: {count_all_comment}\n"
    send_string += "\n\nРейтинг по постам:\n"

    send_string += "\n".join([
        f"{i.get('username'):<20} : {i.get('posts')}"
        for i in sorted(user_stat, key=lambda x: x.get("posts"), reverse=True)
    ])

    send_string += "\n\nРейтинг по комментариям:\n"
    send_string += "\n".join([
        f"  {i.get('username'):<20} : {i.get('comment')}"
        for i in sorted(user_stat, key=lambda x: x.get("comment"), reverse=True)
    ])

    send_mail('ТЕСТ стат', send_string, settings.EMAIL_HOST_USER, ['a03791986@gmail.com'])


@app.task
def add_comment():
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
        for _ in range(random.randint(1, 5))
    ])


@app.task
def add_post():
    category_list = [i["pk"] for i in PostCategory.objects.all().values("pk")]
    author = [i["pk"] for i in User.objects.filter(is_superuser=False).values("pk")]

    PostModel.objects.bulk_create([
        PostModel(
            title="".join([
                random.choice(list(string.ascii_letters) + [" ", ] * 10)
                for _ in range(random.randint(10, 50))
            ]),
            text="".join([
                random.choice(list(string.ascii_letters) + [" ", ] * 10)
                for _ in range(random.randint(100, 1000))
            ]),
            author_id=random.choice(author),
            category_id=random.choice(category_list)
        )
        for _ in range(random.randint(1, 5))
    ])
