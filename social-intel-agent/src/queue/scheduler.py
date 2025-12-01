from celery.schedules import crontab
from src.queue.worker import app

app.conf.beat_schedule = {
    'cleanup-cache': {
        'task': 'src.queue.tasks.cleanup_expired_cache',
        'schedule': crontab(minute=0, hour=0),  # Daily at midnight
    },
}

app.conf.timezone = 'UTC'