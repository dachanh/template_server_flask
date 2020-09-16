import os


class Config:
    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(MODULE_DIR)
    DEBUG = False
    TESTING = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                                       'redis://127.0.0.1:6379/1')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND',
                                           'redis://127.0.0.1:6379/1')
    CELERY_ACCEPT_CONTENT = ['json', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_TRACK_STARTED = True