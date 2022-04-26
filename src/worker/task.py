from src.worker.init_celery import celery
import datetime
from celery.schedules import crontab
from src.models.models import Birthday

celery.conf.enable_utc = False
celery.conf.beat_schedule = {
    "birthday-task": {
        "task": "src.worker.task.birthdays_today",
        "schedule": crontab(minute="*")
    }
}

@celery.task
def birthdays_today():
    today = datetime.datetime.now()
    print("hello")
    print(Birthday.query.all())
