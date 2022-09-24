import logging.config
import os
import pathlib
from datetime import timedelta

from celery import Celery

from conf import config

celery = Celery('Microservice')

PROFILE = os.environ.get('PROFILE') or 'prod'
celery.config_from_object(config[PROFILE], namespace='CELERY')

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
log_conf = PROJECT_ROOT.joinpath('conf').joinpath('logging.conf')
logging.config.fileConfig(log_conf)
logger = logging.getLogger(PROFILE)

__import__('app.user.task', fromlist=['count_user_number_task'])

celery.conf.update(
    CELERYBEAT_SCHEDULE={
        'count-user-task': {
            'task': 'app.user.task.count_user_number_task',
            'schedule': timedelta(minutes=1),  # 每隔1分钟执行一次
            # 'schedule': crontab(minute=4),  # 每小时的第4分钟执行
        },
    }
)

# celery -A worker.celery_app.celery worker -c 100 -P gevent -l INFO
# celery -A worker.celery_app.celery beat -l INFO -s /tmp/celerybeat-schedule
