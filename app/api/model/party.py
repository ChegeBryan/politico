""" Party model """

from app.api.db.mock_db import MockDB
from app.api.model.helper import get_item


class Party:
    """
    Party model class
    """

    def __init__(self, party_name, hq_address, logo_url):
        self.party_name = party_name
        self.hq_address = hq_address
        self.logo_url = logo_url

    def add_party(self):
        """ add a party object to the parties table

        Returns:
            tuple : insert sql query, values(the object initialization
                    attributes)
        """
        query = """INSERT INTO
          parties(party_name, hq_address, logo_url)
          VALUES (%s,%s,%s);
          """
        values = (self.party_name, self.hq_address, self.logo_url)

        return query, values

    @staticmethod
    def get_party_by_name(name):
        """ SQL query to return a party found in the database

        Args:
            name : party name to search for

        Returns:
            tuple : select party sql query
        """
        sql = """SELECT * FROM parties WHERE party_name=%s;"""
        query = sql, (name,)
        return query

    @staticmethod
    def get_party_by_id(identifier):
        """ SQL query to return a party found in the database

        Args:
            identifier : party id

        Returns:
            tuple : select party sql query
        """
        sql = """SELECT * FROM parties WHERE id=%s;"""
        query = sql, (identifier,)
        return query

    @staticmethod
    def update_party(_id, name):
        """ Method to update the name and address of called party """
        party = get_item(_id, MockDB.PARTIES)
        if party:
            party.party_name = name
            return party

    @staticmethod
    def delete_party(_id):
        """ Method to delete party from parties list """
        party = get_item(_id, MockDB.PARTIES)
        if party:
            MockDB.PARTIES.remove(party)
            return True
        else:
            return False
