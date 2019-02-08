"""
app / __init.py
Creation of application factory
"""

from flask import Flask, jsonify

from instance.config import config_environment
from app.api.controller.party_api import parties as parties_bp
from app.api.controller.office_api import offices as office_bp


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

     # Register app error handlers
     @app.errorhandler(405)
     def method_not_allowed(e):
          """
          Json response for Method Not Allowed.
          """
          return jsonify({
               "status": 405,
               "error": "Method Not Allowed on Url."
          }), 405
     # register blueprints to app
     app.register_blueprint(parties_bp, url_prefix='/api/v1')
     app.register_blueprint(office_bp, url_prefix='/api/v1')

     return app
