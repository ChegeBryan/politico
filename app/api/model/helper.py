# functions that are common models.
from app.api.db.mock_db import MockDB


def get_item(identifier, listName):
    """A function to get the selected item from the specified list

    Args:
        identifier (uuid): The id of the item
        listName (list): the list to look loop through
    """
    for item in listName:
        if item._id == identifier:
            return item
