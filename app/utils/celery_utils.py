# app/celery_app.py
from celery import Celery

celery = Celery(
    "compiler_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.update(
    task_track_started=True,
    result_expires=3600,
)
