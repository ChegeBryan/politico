# app environment variables settings
import os


class Config:
    """
    Global configurations environment variables
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET", "dont_show_i_exist")
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    """ Modify Environment variables for development """
    DEBUG = True
    DATABASE_DSN = os.getenv("DEVELOPMENT_DB_DSN")


class ProductionConfig(Config):
    """ Modify environment variable for production """
    DEBUG = False
    TESTING = False
    DATABASE_DSN = os.getenv("PRODUCTION_DB_DSN")

class TestingConfig(Config):
    """ Modify environment variables for testing """
    DEBUG = True
    TESTING = True
    DATABASE_DSN = os.getenv("TESTING_DB_DSN")


config_environment = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
