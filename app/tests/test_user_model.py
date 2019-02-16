# tests for user model

import unittest


from app.api.model.user import User


class UserModelTestCases(unittest.TestCase):
    """
    Class to test if the user required fields are present.
    """
    def setUp(self):
        """
        Creeate the user instance.
        """
        self.new_user = User(
            firstname="peter",
            lastname="simon",
            othername="john",
            email="email@example.com",
            phonenumber="7859393982",
            password="089292",
            passportUrl="https://api.passposts.com/"
        )

    def tearDown(self):
        """ Clears the database"""
        pass


    def test_user_object_creation(self):
        """ Test the user class has been initialized properly """
        self.assertEqual(self.new_user.firstname, 'peter')
        self.assertEqual(self.new_user.lastname, 'simon')
        self.assertEqual(self.new_user.othername, 'john')
        self.assertEqual(self.new_user.email, 'email@example.com')
        self.assertEqual(self.new_user.phonenumber, '7859393982')
        self.assertEqual(self.new_user.password, '089292')
        self.assertEqual(self.new_user.passportUrl,
                         'https://api.passposts.com/')
        self.assertFalse(self.new_user.isAdmin, False)
        self.assertFalse(self.new_user.isPolitician, False)
