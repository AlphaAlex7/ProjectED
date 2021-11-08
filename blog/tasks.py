from celery import shared_task
from .models import PostComment, PostModel
from django.contrib.auth.models import User
from random import choice
import string


@shared_task
def create_new_comment():
    new_com = PostComment(post_id=choice([i.id for i in PostModel.objects.all()]),
                          author=choice(User.objects.all()),
                          text="".join([choice(string.ascii_letters) for _ in range(50)])).save()
    return "ok"
