import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectED.settings')

app = Celery('test_worker')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_stat_for_me': {
        'task': 'blog.tasks.send_stat_for_me',
        'schedule': 60.0,
    },
    'new_posts': {
        'task': 'blog.tasks.add_post',
        'schedule': 30.0,
    },
    'new_comment': {
        'task': 'blog.tasks.add_comment',
        'schedule': 30.0,
    }
}

