""" Office model """


class Office:
    """
    Office model
    """

    def __init__(self, office_name, office_type, is_occupied=False):
        self.office_name = office_name
        self.office_type = office_type
        self.is_occupied = False

    def add_office(self):
        """ add an office object to the parties table

        Returns:
            tuple : insert sql query, values(the object initialization
                    attributes)
        """
        query = """INSERT INTO
          offices(office_name, office_type, is_occupied)
          VALUES (%s,%s,%s) RETURNING id;
          """
        values = (self.office_name, self.office_type, self.is_occupied)

        return query, values

    @staticmethod
    def get_office_by_id(identifier):
        """ SQL query to return a office found in the database

        Args:
            identifier : office id

        Returns:
            tuple : select office sql query
        """
        sql = """SELECT * FROM offices WHERE id=%s;"""
        query = sql, (identifier,)
        return query

    @staticmethod
    def get_office_by_name(name):
        """ SQL query to return a office found in the database

        Args:
            name : office name to search for

        Returns:
            string : select office sql query
        """
        sql = """SELECT * FROM offices WHERE office_name=%s;"""
        query = sql, (name,)
        return query

    @staticmethod
    def get_offices_query():
        """ SQL query to return a parties in the database

        Returns:
            tuple : select party sql query
        """
        sql = """SELECT * FROM offices;"""
        return sql
