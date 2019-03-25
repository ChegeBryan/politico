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
    def get_parties_query():
        """ SQL query to return a parties in the database

        Returns:
            tuple : select party sql query
        """
        sql = """SELECT * FROM parties;"""
        return sql

    @staticmethod
    def update_party(_id, name):
        """ SQL query to update the name of the selected party

        Args:
            _id  : id of the party to edit
            name : party name to change to

        Returns:
            tuple : update party sql query
        """
        sql = """UPDATE parties SET party_name=%s WHERE id=%s;"""
        query = sql, (name, _id)
        return query

    @staticmethod
    def delete_party(_id):
        """ SQL query to delete selected party from the database

        Args:
            _id : party id

        Returns:
            tuple : delete party sql query
        """
        sql = """DELETE FROM parties WHERE id=%s;"""
        query = sql, (_id,)
        return query
