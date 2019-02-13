# database relations.

def drop_table():
    """  Removes tables form the database (TDD) """
    users = """ DROP TABLE IF EXISTS users """
    return users



def create_tables():
    """Create relations in the database"""
    users = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(20) NOT NULL,
        othername VARCHAR(20),
        email VARCHAR(30) NOT NULL,
        phonenumber VARCHAR(24) NOT NULL,
        password VARCHAR(128) NOT NULL,
        passportUrl VARCHAR(256) NOT NULL,
        isAdmin BOOLEAN DEFAULT FALSE,
        isPolitician BOOLEAN DEFAULT FALSE
    );
    """
    return users

def add_admin(conn):
    """ Adds an admin user to the table """
    query = """
    INSERT INTO users(firstname, lastname, email, phonenumber, password, passportUrl, isAdmin) VALUES ('admin', 'user', 'admin@politico.org', '2019nbo37', 'True')"""

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

