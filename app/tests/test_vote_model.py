# test vote class model

import unittest


from app.api.model.vote import Vote


class TestVoteModel(unittest.TestCase):
    """ Test class for vote model """

    def setUp(self):
        """Creation of vote object """
        self.new_vote = Vote(
            office=1,
            candidate=2
        )

    def test_vote_object_creation(self):
        """ Test vote object is initialized properly """
        self.assertEqual(self.new_vote.office, 1)
        self.assertEqual(self.new_vote.candidate, 2)
        self.assertTrue(self.new_vote.created_on)
