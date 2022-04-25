from celery import Celery

redis_uri = 'redis://localhost:6379'
celery = Celery(__name__, backend=redis_uri, broker=redis_uri)

from src.worker.task import birthdays_today