"""
database setup
"""
import psycopg2

from psycopg2.extras import RealDictCursor as dict_cursor


class AppDatabase:

    def __init__(self, dsn):
        """class instance to create a database connection.

        Args:
            dsn (libpd connection string): the connection parameters for the database.
        """
        try:
            self.conn = psycopg2.connect(dsn)
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
