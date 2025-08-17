import os
from celery import Celery

# set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# load settings from Django settings with CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# auto-discover tasks.py in installed apps
app.autodiscover_tasks()
