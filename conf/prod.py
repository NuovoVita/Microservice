# -*- coding: utf-8 -*-

# flask-restful settings.
BUNDLE_ERRORS = False
ERROR_404_HELP = False

# Timezone setting
TIMEZONE = 'Asia/Shanghai'

# Mysql settings.
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:Mjolnir@127.0.0.1:3306/Microservice'
# SQLALCHEMY_ECHO = True

# Redis settings
REDIS_URL = 'redis://:Mjolnir@127.0.0.1:6379/0'

# Security settings.
SECRET_KEY = '447d9aebf0158a652f08223b70828f351db82cda142387cc9a2823a22060656c'
SECRET_SALT = 'ed545f8404cf4a18b042080bf3ac7e3a'

# ES settings.
ELASTICSEARCH_HOST = 'http://Thor:Mjolnir@127.0.0.1:9200'

# celery worker settings.
CELERY_TIMEZONE = TIMEZONE
CELERY_TASK_RESULT_EXPIRES = 300
CELERY_BROKER_URL = 'redis://:Mjolnir@127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://:Mjolnir@127.0.0.1:6379/0'
CELERYD_CONCURRENCY = 1
CELERYD_FORCE_EXECV = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 100

# stream file restore
SRC_STREAM_FILE_FOLDER = '/data/stream_file_data'
RESTORED_STREAM_FOLDER = '/data/restored_stream_folder'
MAX_NUMBER_FILES = 10000

# scheduler task settings.
SCHEDULER_RESULT_BACKEND = REDIS_URL
SCHEDULER_RESULT_CACHE_PREFIX = 'CACHE'
CACHE_DATA_EXPIRE = 7200

# cache rule info redis key.
CACHE_MYSQL_RULE_INFO_KEY = 'CACHE_MYSQL_RULE_INFO_KEY'
CACHE_ES_RULE_INFO_KEY = 'CACHE_ES_RULE_INFO_KEY'

# rule editor settings.
RULE_EDITOR_HOST = 'http://127.0.0.1:8333'
RULE_EDITOR_API_PREFIX = '/api/v1.0'
CUSTOM_RULES_SID_RANGE = [1000000, 2000000]
CUSTOM_RULES_SO_FOLDER = '/data/custom_rules_static'
CUSTOM_RULES_SO_TMP = '/tmp/custom_rules_static'
CUSTOM_RULES_SO_ZIP = 'custom_rules_so.zip'

# packet capture settings.
data_root_pth = '/data4pcap'
interface = 'any'  # 'any' can be used to capture packets from all interfaces.
pcap_size = 300  # 300 is 300 * 1,000,000 bytes.
disk_threshold = 90.0
disk_device_lst = [
    {
        'slot': 1,
        'device_name': 'sdb',
        'mount_point': '/data_sdb',
        'total': 0,
        'used': 0,
        'free': 0,
        'percent': 0,
        'state': 'no_disk',
        'tips': u'无磁盘'
    },
    {
        'slot': 2,
        'device_name': 'sdc',
        'mount_point': '/data_sdc',
        'total': 0,
        'used': 0,
        'free': 0,
        'percent': 0,
        'state': 'no_disk',
        'tips': u'无磁盘'
    }
]

# 设置版本命令：echo "export FRN_VIDEO_CAPTURE_VERSION=1.0.0" > /etc/frn-version
VERSION_INFO = {
    'system': '/etc/frn-version',
    'product_model': 'FTZ-1000S',
    'software_version': '2.0.0',
    'bdmiddleware': '/opt/bdmiddleware/.git_version',
    'data_bridge': '/opt/data_bridge/.git_version',
    'rule_editor': '/opt/rule_editor/.git_version',
    'bdfrontend': '/opt/bdfrontend/dist/.git_version'
}
