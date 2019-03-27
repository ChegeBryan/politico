""" Test Candidate model object creation """

import unittest


from app.api.model.candidate import Candidate


class CandidateModelTestCases(unittest.TestCase):
    """ Candidate model test cases class """

    def setUp(self):
        """create a candidate object instance """
        self.new_candidate = Candidate(
            candidate=1,
            office=2,
            party=2
        )

    def test_candidate_object_creation(self):
        """ Test the candidate instance is initiated properly """
        self.assertTrue(self.new_candidate.created_on)
        self.assertEqual(self.new_candidate.candidate, 1)
        self.assertEqual(self.new_candidate.party, 2)
        self.assertEqual(self.new_candidate.office, 2)
