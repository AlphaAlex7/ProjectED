import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectED.settings')

app = Celery('test_worker')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()
#
# app.conf.beat_schedule = {
#     'create_new_comment': {
#         'task': 'blog.tasks.create_new_comment',
#         'schedule': 15.0,
#     }
# }

