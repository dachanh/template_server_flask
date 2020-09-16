from celery import Celery 

from server_flask.factories.application import create_application
from server_flask.factories.instance_celery import configure_celery 


celery : Celery =  configure_celery(create_application())