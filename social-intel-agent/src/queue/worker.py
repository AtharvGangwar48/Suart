from celery import Celery
from src.config.settings import settings

app = Celery('social_intel_worker')
app.conf.broker_url = settings.redis_url
app.conf.result_backend = settings.redis_url

app.autodiscover_tasks(['src.queue.tasks'])