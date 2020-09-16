from celery import Celery 
from celery.app.task import Task as CeleryTask
from flask import Flask 

from server_flask import extensions 

def configure_celery(app:Flask) -> Celery:
    Taskbase: CeleryTask =  extensions.celery.Task
    
    class ContextCelery(Taskbase):
        abtract =True 
        def __call__(self,*args,**kwargs):
            return Taskbase.__call__(self,*args,**kwargs)
    
    """
    setting celery 
    """
    extensions.celery.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        result_backend=app.config['CELERY_RESULT_BACKEND'],
        accept_content=app.config['CELERY_ACCEPT_CONTENT'],
        task_serializer=app.config['CELERY_TASK_SERIALIZER'],
        result_serializer=app.config['CELERY_TASK_SERIALIZER'],
        worker_hijack_root_logger=False,
        beat_schedule=app.config.get('CELERYBEAT_SCHEDULE', {}),
        worker_redirect_stdouts_level='ERROR',
        task_always_eager=app.config.get('CELERY_ALWAYS_EAGER', False),
        task_create_missing_queues = True
    )
    extensions.celery.Task = ContextCelery
    return extensions.celery