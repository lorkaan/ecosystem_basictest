from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basictest.settings")

import django
django.setup() 

app = Celery("basictest")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()