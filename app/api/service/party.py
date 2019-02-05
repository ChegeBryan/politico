""" Method for data manipulation in the mock db """

from app.api.db.mock_db import MockDB
from app.api.model.party import Party


def save_changes(data):
    """ Write to the mock db """
    MockDB.PARTIES.append(data)
