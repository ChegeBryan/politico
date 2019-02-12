"""
database setup
"""
import psycopg2

from psycopg2.extras import RealDictCursor as dict_cursor


def connect_db(dsn):
    """Creates a connection with the database

    Args:
        dsn : database connection parameters

    Returns:
        a connection to that particular database
    """

    conn = None
    try:
        # create a connection instance to the database
        conn = psycopg2.connect(dsn)

        # create dict cursor instead of the default tuple
        cur = conn.cursor(cursor_factory=dict_cursor)

        # terminate communication to database
        cur.close()
    except(Exception, psycopg2.DatabaseError) as err:
        return err
    finally:
        if conn is not None:
            # close database
            conn.close()

    return conn, cur
