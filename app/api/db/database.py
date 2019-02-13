"""
database setup
"""
import psycopg2

from psycopg2.extras import RealDictCursor as dict_cursor

from app.api.db.db_models import create_tables, drop_tables

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

    def add_tables(self):
        """ Registers all tables to the database """
        queries = create_tables()
        # execute the queries in create_tables methods
        for query in queries:
            self.cur.execute(query)

        self.conn.commit()

    def get_single_row(self, query):
        """ Fetches single data row """
        self.cur.execute(query)
        row = self.cur.fetchone()
        return row

    def get_all_rows(self, query):
        """ Returns the queried rows """
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def commit_changes(self, query, values):
        """ saves the data to database """
        self.cur.execute(query, values)
        self.conn.commit()

    def drop_all(self):
        """ Drop all the relations """
        queries = drop_tables()
        # execute the queries to drop the tables
        for query in queries:
            self.cur.execute(query)

        self.conn.commit()
