"""
app / __init.py
Creation of application factory
"""

from flask import Flask

from instance.config import config_environment
from app.api.controller.party_api import parties as parties_bp
from app.api.controller.party_api import PartiesAPI


def create_app(config_name):
    """
    App creation function

    Args:
        config_name string: environment name

    return:
         flask object
    """
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(config_environment[config_name])

    # register blueprints to app
    app.register_blueprint(parties_bp, url_prefix='/api/v1')

    return app


