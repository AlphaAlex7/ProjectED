import time

from celery import shared_task
from ProjectED.celery_Init import app
from .models import PostComment, PostModel
from django.contrib.auth.models import User
from random import choice
import string
import datetime


@app.task
def create_new_comment(post_id):
    text_comment = f"test celery {datetime.datetime.now()}"+"".join([choice(string.ascii_letters) for _ in range(50)])
    time.sleep(10)
    new_com = PostComment(post_id=post_id,
                          author=choice(User.objects.all()),
                          text=text_comment).save()
    return new_com