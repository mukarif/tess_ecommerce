# test perubahan celery
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# import ..iot.task_celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dash.settings')

app = Celery('dash', backend='redis', broker='redis://localhost:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'update-status-gagal-24jam': {
        'task': 'web.tasks.update_gagal',
        # 'schedule': crontab(minute=1, hour=0),
        'schedule': crontab(minute=0),
        # 'args': (2,)
    },

}

# app.conf.broker_url = 'redis://localhost:6379/0'

# Load task modules from all registered Dja ngo app configs.
app.autodiscover_tasks()

# app.conf.timezone = 'Asia/Jakarta'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
