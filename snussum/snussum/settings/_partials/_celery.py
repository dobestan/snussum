from celery.schedules import crontab


BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'Dating | Match All Users': {
        'task': 'relationships.tasks.datings.match_all',

        # Execute daily at midnight.
        'schedule': crontab(minute=0, hour=0), 
    },
}

CELERY_TIMEZONE = 'Asia/Seoul'
