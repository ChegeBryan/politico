"""
app / __init.py
Creation of application factory
"""

from flask import Flask

from instance.config import config_environment


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

    return app


