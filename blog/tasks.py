import time

from celery import shared_task
from .models import PostComment, PostModel
from django.contrib.auth.models import User
from random import choice
import string


@shared_task
def create_new_comment(post_id):
    time.sleep(10)
    new_com = PostComment(post_id=post_id,
                          author=choice(User.objects.all()),
                          text="".join([choice(string.ascii_letters) for _ in range(50)])).save()
    return "ok"
