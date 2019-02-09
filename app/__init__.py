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

     @app.errorhandler(500)
     def internal_server_error(e):
          """
          custom json response when server hits a 500
          """
          return jsonify({
              "status": 500,
              "error": "Our developers are looking into the issue."
          }), 500

     @app.errorhandler(400)
     def bad_request(e):
          """
          Custom json response for bad request at app level
          """
          return jsonify({
              "status": 400,
              "error": "Check your request format."
          }), 400

     @app.errorhandler(404)
     def url_not_found(e):
          """
          Custom json response for bad request at app level
          """
          return jsonify({
              "status": 404,
              "error": "Check url and try again."
          }), 404

     # register blueprints to app
     app.register_blueprint(parties_bp, url_prefix='/api/v1')
     app.register_blueprint(office_bp, url_prefix='/api/v1')

     return app
