import os
from dotenv import load_dotenv
from celery import Celery
load_dotenv()

redis_uri = os.getenv('REDIS_URI')
celery = Celery(__name__, backend=redis_uri, broker=redis_uri)
