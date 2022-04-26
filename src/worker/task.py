from src.worker.init_celery import celery
import datetime
from celery.schedules import crontab
from src.models.models import Birthday
from src.mail.mail import send_mail

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
    print(Birthday.query.all())
    send_mail()

