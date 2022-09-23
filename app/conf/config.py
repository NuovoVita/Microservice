import os
from urllib.parse import quote_plus


class ProdConfig(object):
    # MySQL settings
    DATABASE_CONNECT_OPTIONS = {}
    DB_HOST = '127.0.0.1'
    USER = 'AntMan'
    PASSWORD = quote_plus('ScottLang@181')
    BASE_DB_NAME = 'Microservice'
    ATTACHED_DB_NAME = 'Statistics'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{USER}:{PASSWORD}@{DB_HOST}:3306/{BASE_DB_NAME}?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        BASE_DB_NAME: SQLALCHEMY_DATABASE_URI,
        ATTACHED_DB_NAME: f'mysql+mysqldb://{USER}:{PASSWORD}@{DB_HOST}:3306/{ATTACHED_DB_NAME}?charset=utf8mb4'}

    # Turn off Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_ECHO = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET'

    SQLALCHEMY_POOL_SIZE = 200

    # Timezone setting
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'

    # Redis settings
    REDIS_URL = 'redis://127.0.0.1:6379/0'
    REDIS_DB0_URL = 'redis://127.0.0.1:6379/0'
    REDIS_DB1_URL = 'redis://127.0.0.1:6379/1'
    REDIS_DB2_URL = 'redis://127.0.0.1:6379/2'
    REDIS_DB3_URL = 'redis://127.0.0.1:6379/3'
    REDIS_DB4_URL = 'redis://127.0.0.1:6379/4'

    # celery worker settings.
    CELERY_TIMEZONE = SCHEDULER_TIMEZONE
    CELERY_ENABLE_UTC = True
    CELERY_TASK_RESULT_EXPIRES = 300
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
    CELERY_CACHE_BACKEND = 'redis://127.0.0.1:6379/0'
    CELERY_TASK_TRACK_STARTED = True
    CELERY_TASK_TIME_LIMIT = 30 * 60
    CELERYD_CONCURRENCY = 1
    CELERYD_FORCE_EXECV = True
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERYD_MAX_TASKS_PER_CHILD = 100
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'


class DevConfig(ProdConfig):
    DB_HOST = '192.168.1.68'
    USER = 'AntMan'
    PASSWORD = quote_plus('ScottLang@181')
    BASE_DB_NAME = 'Microservice'
    ATTACHED_DB_NAME = 'Statistics'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{USER}:{PASSWORD}@{DB_HOST}:3306/{BASE_DB_NAME}?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        BASE_DB_NAME: SQLALCHEMY_DATABASE_URI,
        ATTACHED_DB_NAME: f'mysql+mysqldb://{USER}:{PASSWORD}@{DB_HOST}:3306/{ATTACHED_DB_NAME}_dev?charset=utf8mb4'
    }

    DEBUG = True
    SQLALCHEMY_ECHO = True

    # Redis settings
    REDIS_URL = 'redis://192.168.1.70:6379/0'
    REDIS_DB0_URL = 'redis://192.168.1.70:6379/0'
    REDIS_DB1_URL = 'redis://192.168.1.70:6379/1'
    REDIS_DB2_URL = 'redis://192.168.1.70:6379/2'
    REDIS_DB3_URL = 'redis://192.168.1.70:6379/3'
    REDIS_DB4_URL = 'redis://192.168.1.70:6379/4'


class TestConfig(ProdConfig):
    USER = 'AntMan'
    PASSWORD = quote_plus('ScottLang@181')
    BASE_DB_NAME = 'Microservice'
    ATTACHED_DB_NAME = 'Statistics'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{USER}:{PASSWORD}@127.0.0.1:3306/{BASE_DB_NAME}_test?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        BASE_DB_NAME: SQLALCHEMY_DATABASE_URI,
        ATTACHED_DB_NAME: f'mysql+mysqldb://{USER}:{PASSWORD}@127.0.0.1:3306/{ATTACHED_DB_NAME}_test?charset=utf8mb4'
    }

    # Redis settings
    REDIS_URL = 'redis://:Mjolnir@127.0.0.1:6379/0'
    REDIS_DB0_URL = 'redis://:Mjolnir@127.0.0.1:6379/0'
    REDIS_DB1_URL = 'redis://:Mjolnir@127.0.0.1:6379/1'
    REDIS_DB2_URL = 'redis://:Mjolnir@127.0.0.1:6379/2'
    REDIS_DB3_URL = 'redis://:Mjolnir@127.0.0.1:6379/3'
    REDIS_DB4_URL = 'redis://:Mjolnir@127.0.0.1:6379/4'

    # celery worker settings.
    CELERY_BROKER_URL = 'redis://:Mjolnir@127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'redis://:Mjolnir@127.0.0.1:6379/0'
    CELERY_CACHE_BACKEND = 'redis://:Mjolnir@127.0.0.1:6379/0'
