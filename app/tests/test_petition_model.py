# petition class tests

import unittest


from app.api.model.petition import Petition


class PetitionModelTestCases(unittest.TestCase):
    """ Test class for petition model """

    def setUp(self):
        """Create a petition object instance
        :arg: office, created_by, body, evidence
        :return: petition instance
        """
        self.new_petition = Petition(
            office=1,
            contested_by=2,
            created_by=2,
            body='Some reason for the petition',
            evidence='http://get.go.com'
        )

    def test_petition_object_creation(self):
        """ test petition object is instantiated properly """
        self.assertEqual(self.new_petition.office, 1)
        self.assertEqual(self.new_petition.contested_by, 2)
        self.assertEqual(self.new_petition.contested_by, 2)
        self.assertEqual(self.new_petition.body,
                         'Some reason for the petition')
        self.assertEqual(self.new_petition.evidence, 'http://get.go.com')
        self.assertTrue(self.new_petition.created_on)
