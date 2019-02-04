# test application configurations in different environment

import unittest

from app import create_app


class TestConfig(unittest.TestCase):
    """
    Test environment variables configure correctly in different environments
    """
    def test_app_environment_development(self):
        app = create_app("development")
        self.assertTrue(app.config["DEBUG"] is True)

