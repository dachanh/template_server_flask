from flask import Flask 
from server_flask.controllers.submit_api import api as submit_api
from server_flask.factories.configuration import Config 


def create_application()-> Flask:
    app =  Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(submit_api)
    return app