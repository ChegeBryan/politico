"""
Method for data manipulation between controller and models
in the mock db
"""

from app.api.db.mock_db import MockDB



def save_changes(data):
    """ Write to the mock db """
    MockDB.OFFICES.append(data)

