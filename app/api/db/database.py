"""
database setup
"""
import psycopg2

from flask import current_app

from psycopg2.extras import RealDictCursor as dict_cursor
from app.api.db.db_models import create_tables, drop_tables, add_admin


class AppDatabase:
    """Database connection class
    Methods that:
       1. connect to database
       2. write, read and update database entries reside here.
    """

    def __init__(self):
        """class instance to create a database connection.

        Args:
            dsn (libpd connection string): the connection parameters for the
            database.
            When the class is initialized a connection to the database is
            established depending on the environment the app is running at.
        """
        try:
            dsn = current_app.config["DATABASE_DSN"]
            self.conn = psycopg2.connect(dsn)
            self.cur = self.conn.cursor(cursor_factory=dict_cursor)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_tables(self):
        """ Registers all tables to the database """
        queries = create_tables()
        # execute the queries in create_tables methods
        for query in queries:
            self.cur.execute(query)

        self.conn.commit()

    def add_default_admin(self):
        """Register a default admin user for the app"""
        query = add_admin()
        self.cur.execute(*query)
        self.conn.commit()

    def get_single_row(self, query, value):
        """ Fetches single data row """
        self.cur.execute(query, value)
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

    def commit_changes_returning_id(self, query, values):
        """ saves the data to database and
        return primary key of saved data
        """
        self.cur.execute(query, values)
        identifier = self.cur.fetchone()['id']
        self.conn.commit()
        return identifier

    def drop_all(self):
        """ Drop all the relations """
        queries = drop_tables()
        # execute the queries to drop the tables
        for query in queries:
            self.cur.execute(query)
        self.conn.commit()
