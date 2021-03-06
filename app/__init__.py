"""
app / __init.py
Creation of application factory
"""

from flask import Flask
from flask_cors import CORS

from instance.config import config_environment
from app.api.db.database import AppDatabase
from app.api.util.error_handlers import (bad_request, internal_server_error,
                                         url_not_found, method_not_allowed)
from app.api.controller.party_api import parties as parties_bp
from app.api.controller.office_api import offices as offices_bp
from app.api.controller.user_api import users as users_bp
from app.api.controller.auth import auth as auth_bp
from app.api.controller.candidate_api import candidates as candidates_bp
from app.api.controller.vote_api import votes as votes_bp
from app.api.controller.result_api import results as results_bp
from app.api.controller.petition_api import petitions as petitions_bp
from app.api.controller.application_api import application as application_bp


def create_app(config_name):
    """App creation function
    Args:
       config_name string: environment name
    return:
       flask object
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_environment[config_name])
    app.url_map.strict_slashes = False
    CORS(app)

    # create database connection based on the application context
    with app.app_context():
        db = AppDatabase()
        db.add_tables()
        db.add_default_admin()

    # register error handlers
    app.register_error_handler(400, bad_request)
    app.register_error_handler(404, url_not_found)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(405, method_not_allowed)

    # register blueprints to app
    app.register_blueprint(parties_bp, url_prefix='/api/v2')
    app.register_blueprint(offices_bp, url_prefix='/api/v2')
    app.register_blueprint(users_bp, url_prefix='/api/v2')
    app.register_blueprint(auth_bp, url_prefix='/api/v2')
    app.register_blueprint(candidates_bp, url_prefix='/api/v2')
    app.register_blueprint(votes_bp, url_prefix='/api/v2')
    app.register_blueprint(results_bp, url_prefix='/api/v2')
    app.register_blueprint(petitions_bp, url_prefix='/api/v2')
    app.register_blueprint(application_bp, url_prefix='/api/v2')

    return app
