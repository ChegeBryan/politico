""" Test application model object creation """

import unittest


from app.api.model.application import Application


class ApplicationModelTestCases(unittest.TestCase):
    """ Application model test cases class """

    def setUp(self):
        """Create an application class instance """
        self.new_application = Application(
            party=2,
            office=2
        )

    def test_application_object_creation(self):
        """ Test the application instance is initialized properly """
        self.assertTrue(self.new_application.party, 2)
        self.assertTrue(self.new_application.office, 2)
        self.assertTrue(self.new_application.requested_on)
