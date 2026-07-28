import os
from celery import Celery

# Set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basictest.settings")

# Create Celery app
app = Celery("basictest")

# Load config from Django settings (CELERY_ namespace)
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py in installed apps
app.autodiscover_tasks()