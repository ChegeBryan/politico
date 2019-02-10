"""
app / __init.py
Creation of application factory
"""

from flask import Flask, jsonify

from instance.config import config_environment
from app.api.util.error_handlers import bad_request, internal_server_error, url_not_found, method_not_allowed
from app.api.controller.party_api import parties as parties_bp
from app.api.controller.office_api import offices as offices_bp


def create_app(config_name):
    """

    App creation function
    Args:
       config_name string: environment name
    return:
       flask object
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_environment[config_name])

    # register error handlers
    app.register_error_handler(400, bad_request)
    app.register_error_handler(404, url_not_found)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(405, method_not_allowed)

    # register blueprints to app
    app.register_blueprint(parties_bp, url_prefix='/api/v1')
    app.register_blueprint(offices_bp, url_prefix='/api/v1')

    return app
