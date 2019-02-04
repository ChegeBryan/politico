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


class DevelopmentConfig(Config):
    """ Modify Environment variables for development """
    DEBUG = True


class ProductionConfig(Config):
    """ Modify environment variable for production """
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """ Modify environment variables for testing """
    DEBUG = True
    TESTING = True


config_environment = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
